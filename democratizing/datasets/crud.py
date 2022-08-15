from democratizing.models import DatasetAlias, AgencyRun
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_datasets(pagination: PaginationParams, db: Session):
    return apply_pagination(
        db.query(
            DatasetAlias.id,
            DatasetAlias.run_id,
            DatasetAlias.parent_alias_id,
            DatasetAlias.alias_id,
            DatasetAlias.alias_type,
            DatasetAlias.alias,
            DatasetAlias.url,
            DatasetAlias.last_updated_date,
            AgencyRun.agency,
            AgencyRun.version,
        ).join(AgencyRun, DatasetAlias.run_id == AgencyRun.id),
        pagination,
    ).all()
