from democratizing.models import PublicationAffiliation
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_publication_affiliations(pagination: PaginationParams, db: Session) -> list[PublicationAffiliation]:
    return apply_pagination(db.query(PublicationAffiliation), pagination).all()
