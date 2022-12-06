from democratizing.models import Dyad, AgencyRun
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_dyads(pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[Dyad]:
    if (agency):
        return apply_pagination(
            db.query(Dyad)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency),
            pagination
        ).all()
    else:
        return apply_pagination(db.query(Dyad), pagination).all()
