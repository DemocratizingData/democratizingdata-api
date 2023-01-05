from democratizing.models import Topic, Publication, PublicationTopic, Author, PublicationAuthor, DatasetAlias, Dyad, AgencyRun, AuthorAffiliation, PublicationAffiliation
from sqlalchemy.orm import Session
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from typing import Union
import logging

logger = logging.getLogger()


def get_topics(pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[Topic]:
    if (agency):
        return apply_pagination(
            db.query(Topic)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency),
            pagination
        ).all()
    else:
        return apply_pagination(db.query(Topic), pagination).all()


def get_topic_publications(topic_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[Publication]:
    if (agency):
        return apply_pagination(
            db.query(Publication)
            .join(PublicationTopic)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency)
            .filter(PublicationTopic.topic_id == topic_id),
            pagination,
        ).all()
    else:
        return apply_pagination(
            db.query(Publication)
            .join(PublicationTopic)
            .filter(PublicationTopic.topic_id == topic_id),
            pagination,
        ).all()

def get_topic_authors(topic_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]):
    if (agency):
        return apply_pagination(
            db.query(
                Author.id,
                Author.run_id,
                Author.external_id,
                Author.given_name,
                Author.family_name,
                Author.last_updated_date,
                PublicationAffiliation.institution_name,
                PublicationAffiliation.address,
                PublicationAffiliation.city,
                PublicationAffiliation.state,
                PublicationAffiliation.country_code,
                PublicationAffiliation.postal_code)
            .join(PublicationAuthor)
            .join(AuthorAffiliation)
            .join(PublicationAffiliation)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency)
            .filter(PublicationTopic.topic_id == topic_id),
            pagination,
        ).all()
    else:
        return apply_pagination(
            db.query(
                Author.id,
                Author.run_id,
                Author.external_id,
                Author.given_name,
                Author.family_name,
                Author.last_updated_date,
                PublicationAffiliation.institution_name,
                PublicationAffiliation.address,
                PublicationAffiliation.city,
                PublicationAffiliation.state,
                PublicationAffiliation.country_code,
                PublicationAffiliation.postal_code)
            .join(PublicationAuthor)
            .join(AuthorAffiliation)
            .join(PublicationAffiliation)
            .join(Publication)
            .join(PublicationTopic)
            .filter(PublicationTopic.topic_id == topic_id),
            pagination,
        ).all()

def get_topic_datasets(topic_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[DatasetAlias]:
    if (agency):
        return apply_pagination(
            db.query(DatasetAlias)
            .join(Dyad)
            .join(Publication)
            .join(PublicationTopic)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency)
            .filter(PublicationTopic.topic_id == topic_id),
            pagination,
        ).all()
    else:
        return apply_pagination(
            db.query(DatasetAlias)
            .join(Dyad)
            .join(Publication)
            .join(PublicationTopic)
            .filter(PublicationTopic.topic_id == topic_id),
            pagination,
        ).all()
