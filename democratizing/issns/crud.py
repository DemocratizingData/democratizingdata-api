from democratizing.models import ISSN
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_issns(pagination: PaginationParams, db: Session) -> list[ISSN]:
    return apply_pagination(db.query(ISSN), pagination).all()
