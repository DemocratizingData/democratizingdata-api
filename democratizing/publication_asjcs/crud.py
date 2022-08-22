from democratizing.models import PublicationAsjc
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_publication_asjcs(
    pagination: PaginationParams, db: Session
) -> list[PublicationAsjc]:
    return apply_pagination(db.query(PublicationAsjc), pagination).all()
