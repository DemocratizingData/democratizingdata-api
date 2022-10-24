from democratizing.models import PublicationTopic
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_publication_topics(
    pagination: PaginationParams, db: Session
) -> list[PublicationTopic]:
    return apply_pagination(db.query(PublicationTopic), pagination).all()
