from democratizing.models import PublicationDatasetAlias
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_publication_dataset_aliases(
    pagination: PaginationParams, db: Session
) -> list[PublicationDatasetAlias]:
    return apply_pagination(db.query(PublicationDatasetAlias), pagination).all()
