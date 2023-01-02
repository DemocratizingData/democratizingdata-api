from democratizing.models import AgencyRun, Publication, PublicationAffiliation, AuthorAffiliation, \
    Author, PublicationAuthor
from democratizing.utils import apply_pagination
from democratizing.dependencies import PaginationParams
from sqlalchemy.orm import Session
from typing import Union
import logging

logger = logging.getLogger()


def get_full_authors(pagination: PaginationParams, db: Session, agency: Union[str, None]):
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
                PublicationAffiliation.postal_code
            ).join(PublicationAuthor)
            .join(AuthorAffiliation)
            .join(PublicationAffiliation)
            .join(AgencyRun)
            .filter(AgencyRun.agency == agency),
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
                PublicationAffiliation.postal_code
            ).join(PublicationAuthor)
            .join(AuthorAffiliation)
            .join(PublicationAffiliation),
            pagination,
        ).all()
