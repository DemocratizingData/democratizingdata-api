from democratizing.models import PublicationTopic, AgencyRun
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_publication_topics(
    pagination: PaginationParams, db: Session, agency: Union[str, None]
) -> list[PublicationTopic]:
    if (agency):
        return apply_pagination(
            db.query(PublicationTopic)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency),
            pagination).all()
    else:
        return apply_pagination(db.query(PublicationTopic), pagination).all()
