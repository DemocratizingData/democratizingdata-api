from democratizing.models import Author, Topic, Publication, DatasetAlias, PublicationAuthor, PublicationTopic, PublicationDatasetAlias
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_authors(pagination: PaginationParams, db: Session) -> list[Author]:
    return apply_pagination(db.query(Author), pagination).all()

def get_author_topics(author_id: int, pagination: PaginationParams, db: Session) -> list[Topic]:
    return apply_pagination(
        db.query(Topic)
        .join(PublicationTopic)
        .join(Publication)
        .join(PublicationAuthor)
        .filter(PublicationAuthor.author_id == author_id),
        pagination,
    ).all()


def get_author_publications(author_id: int, pagination: PaginationParams, db: Session) -> list[Publication]:
    return apply_pagination(
        db.query(Publication)
        .join(PublicationAuthor)
        .filter(PublicationAuthor.author_id == author_id),
        pagination,
    ).all()


def get_author_datasets(author_id: int, pagination: PaginationParams, db: Session) -> list[DatasetAlias]:
    return apply_pagination(
        db.query(DatasetAlias)
        .join(PublicationDatasetAlias)
        .join(Publication)
        .join(PublicationAuthor)
        .filter(PublicationAuthor.author_id == author_id),
        pagination,
    ).all()