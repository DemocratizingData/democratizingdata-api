from democratizing.models import DatasetAlias, AgencyRun, Publication, Dyad, Topic, PublicationTopic, \
    Author, PublicationAuthor, AuthorAffiliation, PublicationAffiliation
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_datasets(pagination: PaginationParams, db: Session, agency: Union[str, None]):
    if (agency):
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
            ).join(AgencyRun)
            .filter(AgencyRun.agency == agency),
            pagination,
        ).all()
    else:
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


def get_dataset_publications(parent_alias_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]):
    if (agency):
        return apply_pagination(
            db.query(Publication)
            .join(Dyad)
            .join(DatasetAlias)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency)
            .filter(DatasetAlias.parent_alias_id == parent_alias_id),
            pagination,
        ).all()
    else:
        return apply_pagination(
            db.query(Publication)
            .join(Dyad)
            .join(DatasetAlias)
            .filter(DatasetAlias.parent_alias_id == parent_alias_id),
            pagination,
        ).all()


def get_dataset_topics(parent_alias_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]):
    if (agency):
        return apply_pagination(
            db.query(Topic)
            .join(PublicationTopic)
            .join(Publication)
            .join(Dyad)
            .join(DatasetAlias)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency)
            .filter(DatasetAlias.parent_alias_id == parent_alias_id),
            pagination,
        ).all()
    else:
        return apply_pagination(
            db.query(Topic)
            .join(PublicationTopic)
            .join(Publication)
            .join(Dyad)
            .join(DatasetAlias)
            .filter(DatasetAlias.parent_alias_id == parent_alias_id),
            pagination,
        ).all()


def get_dataset_authors(parent_alias_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]):
    if (agency):
        return apply_pagination(
            db.query(
                Author.id,
                Author.run_id,
                Author.external_id,
                Author.given_name,
                Author.family_name,
                Author.last_updated_date,
                PublicationAffiliation.institution_name,
                PublicationAffiliation.address,
                PublicationAffiliation.city,
                PublicationAffiliation.state,
                PublicationAffiliation.country_code,
                PublicationAffiliation.postal_code)
            .join(PublicationAuthor)
            .join(Publication)
            .join(AuthorAffiliation)
            .join(PublicationAffiliation)
            .join(Dyad)
            .join(DatasetAlias)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency)
            .filter(DatasetAlias.parent_alias_id == parent_alias_id),
            pagination,
        ).all()
    else:
        return apply_pagination(
            db.query(
                Author.id,
                Author.run_id,
                Author.external_id,
                Author.given_name,
                Author.family_name,
                Author.last_updated_date,
                PublicationAffiliation.institution_name,
                PublicationAffiliation.address,
                PublicationAffiliation.city,
                PublicationAffiliation.state,
                PublicationAffiliation.country_code,
                PublicationAffiliation.postal_code)
            .join(PublicationAuthor)
            .join(Publication)
            .join(AuthorAffiliation)
            .join(PublicationAffiliation)
            .join(Dyad)
            .join(DatasetAlias)
            .filter(DatasetAlias.parent_alias_id == parent_alias_id),
            pagination,
        ).all()


def get_dataset_aliases(parent_alias_id: int, pagination: PaginationParams, db: Session, agency: Union[str, None]):
    if (agency):
        return apply_pagination(
            db.query(DatasetAlias)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency)
            .filter(DatasetAlias.parent_alias_id == parent_alias_id),
            pagination,
        ).all()
    else:
        return apply_pagination(
            db.query(DatasetAlias)
            .filter(DatasetAlias.parent_alias_id == parent_alias_id),
            pagination,
        ).all()
