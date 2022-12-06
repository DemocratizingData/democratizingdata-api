from democratizing.models import Author, Topic, Publication, DatasetAlias, PublicationAuthor, PublicationTopic, Dyad, AgencyRun
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_authors(pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[Author]:
    if (agency):
        return apply_pagination(
            db.query(Author)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency),
            pagination
        ).all()
    else:
        return apply_pagination(db.query(Author), pagination).all()

def get_author_topics(author_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[Topic]:
    if (agency):
        return apply_pagination(
            db.query(Topic)
            .join(PublicationTopic)
            .join(Publication)
            .join(PublicationAuthor)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency)
            .filter(PublicationAuthor.author_id == author_id),
            pagination,
        ).all()
    else:
        return apply_pagination(
            db.query(Topic)
            .join(PublicationTopic)
            .join(Publication)
            .join(PublicationAuthor)
            .filter(PublicationAuthor.author_id == author_id),
            pagination,
        ).all()


def get_author_publications(author_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[Publication]:
    if (agency):
        return apply_pagination(
            db.query(Publication)
            .join(PublicationAuthor)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency)
            .filter(PublicationAuthor.author_id == author_id),
            pagination,
        ).all()
    else:
        return apply_pagination(
            db.query(Publication)
            .join(PublicationAuthor)
            .filter(PublicationAuthor.author_id == author_id),
            pagination,
        ).all()

def get_author_datasets(author_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[DatasetAlias]:
    if (agency):
        return apply_pagination(
            db.query(DatasetAlias)
            .join(Dyad)
            .join(Publication)
            .join(PublicationAuthor)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency)
            .filter(PublicationAuthor.author_id == author_id),
            pagination,
        ).all()
    else:
        return apply_pagination(
            db.query(DatasetAlias)
            .join(Dyad)
            .join(Publication)
            .join(PublicationAuthor)
            .filter(PublicationAuthor.author_id == author_id),
            pagination,
        ).all()