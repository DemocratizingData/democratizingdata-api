from democratizing.models import Affiliation, AgencyRun
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_affiliations(pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[Affiliation]:
    if (agency):
        return apply_pagination(
            db.query(Affiliation)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency),
            pagination
        ).all()
    else:
        return apply_pagination(db.query(Affiliation), pagination).all()
