from democratizing.models import Affiliation
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_affiliations(pagination: PaginationParams, db: Session) -> list[Affiliation]:
    return apply_pagination(db.query(Affiliation), pagination).all()
