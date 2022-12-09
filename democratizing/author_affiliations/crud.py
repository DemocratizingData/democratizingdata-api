from democratizing.models import AuthorAffiliation, AgencyRun
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_author_affiliations(
    pagination: PaginationParams, db: Session, agency: Union[str, None]
) -> list[AuthorAffiliation]:
    if agency:
        return apply_pagination(
            db.query(AuthorAffiliation)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency), pagination).all()
    else:
        return apply_pagination(db.query(AuthorAffiliation), pagination).all()
