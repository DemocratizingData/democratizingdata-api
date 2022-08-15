from democratizing.models import AgencyRun
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_agency_runs(pagination: PaginationParams, db: Session) -> list[AgencyRun]:
    return apply_pagination(db.query(AgencyRun), pagination).all()
