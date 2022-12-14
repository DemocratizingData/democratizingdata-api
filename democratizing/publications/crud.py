from democratizing.models import Publication, Topic, DatasetAlias, Author, PublicationTopic, PublicationAuthor, Dyad, AgencyRun, AuthorAffiliation, PublicationAffiliation
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_publications(pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[Publication]:
    if (agency):
        return apply_pagination(
            db.query(Publication)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency),
            pagination
        ).all()
    else:
        return apply_pagination(
            db.query(Publication),
            pagination
        ).all()

def get_publication_topics(publication_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[Topic]:
    if (agency):
        return apply_pagination(
            db.query(Topic)
            .join(PublicationTopic)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency)
            .filter(PublicationTopic.publication_id == publication_id),
            pagination,
        ).all()
    else:
        return apply_pagination(
            db.query(Topic)
            .join(PublicationTopic)
            .filter(PublicationTopic.publication_id == publication_id),
            pagination,
        ).all()


def get_publication_authors(publication_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]):
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
            .filter(PublicationAuthor.publication_id == publication_id),
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
            .filter(PublicationAuthor.publication_id == publication_id),
            pagination,
        ).all()


def get_publication_datasets(publication_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[DatasetAlias]:
    if (agency):
        return apply_pagination(
            db.query(DatasetAlias)
            .join(Dyad)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency)
            .filter(Dyad.publication_id == publication_id),
            pagination,
        ).all()
    else:
        return apply_pagination(
            db.query(DatasetAlias)
            .join(Dyad)
            .filter(Dyad.publication_id == publication_id),
            pagination,
        ).all()