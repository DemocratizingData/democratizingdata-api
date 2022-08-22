from democratizing.models import Asjc
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_asjcs(pagination: PaginationParams, db: Session) -> list[Asjc]:
    return apply_pagination(db.query(Asjc), pagination).all()
