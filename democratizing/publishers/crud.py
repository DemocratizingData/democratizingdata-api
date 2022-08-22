from democratizing.models import Publisher
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_publishers(pagination: PaginationParams, db: Session) -> list[Publisher]:
    return apply_pagination(db.query(Publisher), pagination).all()
