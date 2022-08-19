from democratizing.models import PdaModel
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_pda_models(pagination: PaginationParams, db: Session) -> list[PdaModel]:
    return apply_pagination(db.query(PdaModel), pagination).all()
