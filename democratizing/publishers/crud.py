from democratizing.models import Publisher, AgencyRun
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_publishers(pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[Publisher]:
    if (agency):
        return apply_pagination(
            db.query(Publisher)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency),
            pagination).all()
    else:
        return apply_pagination(db.query(Publisher), pagination).all()
