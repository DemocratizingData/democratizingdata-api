from democratizing.models import Publication
from democratizing.utils import apply_limit_offset
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_publications(pagination: PaginationParams, db: Session):
    return apply_limit_offset(db.query(Publication), pagination).all()
