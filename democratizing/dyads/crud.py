from democratizing.models import Dyad
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_dyads(
    pagination: PaginationParams, db: Session
) -> list[Dyad]:
    return apply_pagination(db.query(Dyad), pagination).all()
