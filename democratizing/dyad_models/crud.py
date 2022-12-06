from democratizing.models import DyadModel, AgencyRun
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_dyad_models(pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[DyadModel]:
    if (agency):
        return apply_pagination(
            db.query(DyadModel)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency),
            pagination
        ).all()
    else:
        return apply_pagination(db.query(DyadModel), pagination).all()
