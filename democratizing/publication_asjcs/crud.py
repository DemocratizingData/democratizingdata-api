from democratizing.models import PublicationAsjc, AgencyRun
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_publication_asjcs(
    pagination: PaginationParams, db: Session, agency: Union[str, None]
) -> list[PublicationAsjc]:
    if (agency):
        return apply_pagination(
            db.query(PublicationAsjc)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency), pagination).all()
    else:
        return apply_pagination(db.query(PublicationAsjc), pagination).all()
