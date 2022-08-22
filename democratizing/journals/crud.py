from democratizing.models import Journal
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_journals(pagination: PaginationParams, db: Session) -> list[Journal]:
    return apply_pagination(db.query(Journal), pagination).all()
