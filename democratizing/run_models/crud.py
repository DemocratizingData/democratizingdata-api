from democratizing.models import Model, AgencyRun, DyadModel
from sqlalchemy.orm import Session
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from typing import Union
import logging

logger = logging.getLogger()


def get_models(pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[Model]:
    if (agency):
        return apply_pagination(
            db.query(Model)
            .join(DyadModel)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency),
            pagination).all()
    else:
        return apply_pagination(
            db.query(Model),
            pagination).all()