from democratizing.models import Model
from sqlalchemy.orm import Session
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
import logging

logger = logging.getLogger()


def get_models(pagination: PaginationParams, db: Session) -> list[Model]:
    return apply_pagination(db.query(Model), pagination).all()
