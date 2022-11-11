from democratizing.models import Topic, Publication, PublicationTopic, Author, PublicationAuthor, DatasetAlias, PublicationDatasetAlias
from sqlalchemy.orm import Session
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
import logging

logger = logging.getLogger()


def get_topics(pagination: PaginationParams, db: Session) -> list[Topic]:
    return apply_pagination(db.query(Topic), pagination).all()


def get_topic_publications(
    topic_id: int, pagination: PaginationParams, db: Session
) -> list[Publication]:
    return apply_pagination(
        db.query(Publication)
        .join(PublicationTopic)
        .filter(PublicationTopic.topic_id == topic_id),
        pagination,
    ).all()

def get_topic_authors(
    topic_id: int, pagination: PaginationParams, db: Session
) -> list[Author]:
    return apply_pagination(
        db.query(Author)
        .join(PublicationAuthor)
        .join(Publication)
        .join(PublicationTopic)
        .filter(PublicationTopic.topic_id == topic_id),
        pagination,
    ).all()

def get_topic_datasets(
    topic_id: int, pagination: PaginationParams, db: Session
) -> list[DatasetAlias]:
    return apply_pagination(
        db.query(DatasetAlias)
        .join(PublicationDatasetAlias)
        .join(Publication)
        .join(PublicationTopic)
        .filter(PublicationTopic.topic_id == topic_id),
        pagination,
    ).all()
