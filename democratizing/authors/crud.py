from democratizing.models import Author
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_authors(pagination: PaginationParams, db: Session) -> list[Author]:
    return apply_pagination(db.query(Author), pagination).all()
