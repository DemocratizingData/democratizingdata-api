from democratizing.models import Journal, AgencyRun
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_journals(pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[Journal]:
    if (agency):
        return apply_pagination(
            db.query(Journal)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency),
            pagination).all()
    else:
        return apply_pagination(
            db.query(Journal),
            pagination).all()
