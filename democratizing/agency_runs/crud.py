from democratizing.models import AgencyRun
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_agency_runs(pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[AgencyRun]:
    if agency:
        return apply_pagination(
            db.query(AgencyRun)
            .filter(AgencyRun.agency == agency),
            pagination).all()
    else:
        return apply_pagination(
            db.query(AgencyRun),
            pagination).all()
