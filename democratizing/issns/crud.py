from democratizing.models import ISSN, AgencyRun
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_issns(pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[ISSN]:
    if (agency):
        return apply_pagination(
            db.query(ISSN)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency),
            pagination).all()
    else:
        return apply_pagination(
            db.query(ISSN),
            pagination).all()