from democratizing.models import AuthorAffiliation
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_author_affiliations(
    pagination: PaginationParams, db: Session
) -> list[AuthorAffiliation]:
    return apply_pagination(db.query(AuthorAffiliation), pagination).all()
