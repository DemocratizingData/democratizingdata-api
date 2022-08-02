from democratizing.models import Publication
from democratizing.utils import apply_limit_offset
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_publications(limit: int | None, offset: int | None, db: Session):
    return apply_limit_offset(db.query(Publication), limit, offset).all()
