from democratizing.models import Topic, Publication, PublicationTopic, Author, PublicationAuthor, DatasetAlias, PublicationDatasetAlias, AgencyRun
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


def get_topic_publications(
    topic_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]
) -> list[Publication]:
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
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency)
            .filter(PublicationTopic.topic_id == topic_id),
            pagination,
        ).all()

def get_topic_authors(
    topic_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]
) -> list[Author]:
    if (agency):
        return apply_pagination(
            db.query(Author)
            .join(PublicationAuthor)
            .join(Publication)
            .join(PublicationTopic)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency)
            .filter(PublicationTopic.topic_id == topic_id),
            pagination,
        ).all()
    else:
        return apply_pagination(
            db.query(Author)
            .join(PublicationAuthor)
            .join(Publication)
            .join(PublicationTopic)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency)
            .filter(PublicationTopic.topic_id == topic_id),
            pagination,
        ).all()

def get_topic_datasets(
    topic_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]
) -> list[DatasetAlias]:
    if (agency):
        return apply_pagination(
            db.query(DatasetAlias)
            .join(PublicationDatasetAlias)
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
            .join(PublicationDatasetAlias)
            .join(Publication)
            .join(PublicationTopic)
            .filter(PublicationTopic.topic_id == topic_id),
            pagination,
        ).all()
