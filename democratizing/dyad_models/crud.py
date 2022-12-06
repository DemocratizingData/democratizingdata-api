from democratizing.models import DyadModel
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_dyad_models(pagination: PaginationParams, db: Session) -> list[DyadModel]:
    return apply_pagination(db.query(DyadModel), pagination).all()
