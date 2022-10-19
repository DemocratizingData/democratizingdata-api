from democratizing.models import Publication, Topic, DatasetAlias, Author, PublicationTopic, PublicationAuthor, PublicationDatasetAlias
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_publications(pagination: PaginationParams, db: Session) -> list[Publication]:
    return apply_pagination(db.query(Publication), pagination).all()

def get_publication_topics(publication_id: int, pagination: PaginationParams, db: Session) -> list[Topic]:
    return apply_pagination(
        db.query(Topic)
        .join(PublicationTopic)
        .filter(PublicationTopic.publication_id == publication_id),
        pagination,
    ).all()


def get_publication_authors(publication_id: int, pagination: PaginationParams, db: Session) -> list[Author]:
    return apply_pagination(
        db.query(Author)
        .join(PublicationAuthor)
        .filter(PublicationAuthor.publication_id == publication_id),
        pagination,
    ).all()


def get_publication_datasets(publication_id: int, pagination: PaginationParams, db: Session) -> list[DatasetAlias]:
    return apply_pagination(
        db.query(DatasetAlias)
        .join(PublicationDatasetAlias)
        .filter(PublicationDatasetAlias.publication_id == publication_id),
        pagination,
    ).all()