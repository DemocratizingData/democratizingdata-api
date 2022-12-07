from democratizing.models import PdaModel, AgencyRun
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_pda_models(pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[PdaModel]:
    if (agency):
        return apply_pagination(
            db.query(PdaModel)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency),
            pagination
        ).all()
    else:
        return apply_pagination(db.query(PdaModel), pagination).all()
