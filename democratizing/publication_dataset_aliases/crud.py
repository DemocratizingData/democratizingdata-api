from democratizing.models import PublicationDatasetAlias, AgencyRun
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_publication_dataset_aliases(pagination: PaginationParams, db: Session, agency: Union[str, None]) -> list[PublicationDatasetAlias]:
    if (agency):
        return apply_pagination(
            db.query(PublicationDatasetAlias)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency),
            pagination
        ).all()
    else:
        return apply_pagination(db.query(PublicationDatasetAlias), pagination).all()
