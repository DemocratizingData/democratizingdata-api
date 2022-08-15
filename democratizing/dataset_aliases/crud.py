from democratizing.models import DatasetAlias
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_dataset_aliases(
    pagination: PaginationParams, db: Session
) -> list[DatasetAlias]:
    return apply_pagination(db.query(DatasetAlias), pagination).all()
