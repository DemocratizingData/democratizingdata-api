from democratizing.models import DatasetAlias, AgencyRun, Publication, PublicationDatasetAlias, Topic, PublicationTopic, Author, PublicationAuthor
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
        ).join(AgencyRun),
        pagination,
    ).all()

def get_dataset_publications(parent_alias_id: int, pagination: PaginationParams, db: Session):
    return apply_pagination(
        db.query(Publication)
        .join(PublicationDatasetAlias)
        .join(DatasetAlias)
        .filter(DatasetAlias.parent_alias_id == parent_alias_id),
        pagination,
    ).all()

def get_dataset_topics(parent_alias_id: int, pagination: PaginationParams, db: Session):
    return apply_pagination(
        db.query(Topic)
        .join(PublicationTopic)
        .join(Publication)
        .join(PublicationDatasetAlias)
        .join(DatasetAlias)
        .filter(DatasetAlias.parent_alias_id == parent_alias_id),
        pagination,
    ).all()

def get_dataset_authors(parent_alias_id: int, pagination: PaginationParams, db: Session):
    return apply_pagination(
        db.query(Author)
        .join(PublicationAuthor)
        .join(Publication)
        .join(PublicationDatasetAlias)
        .join(DatasetAlias)
        .filter(DatasetAlias.parent_alias_id == parent_alias_id),
        pagination,
    ).all()


def get_dataset_aliases(parent_alias_id: int, pagination: PaginationParams, db: Session):
    return apply_pagination(
        db.query(DatasetAlias)
        .filter(DatasetAlias.parent_alias_id == parent_alias_id),
        pagination,
    ).all()
