from democratizing.models import PublicationAuthor
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_publication_authors(pagination: PaginationParams, db: Session) -> list[PublicationAuthor]:
    return apply_pagination(db.query(PublicationAuthor), pagination).all()
