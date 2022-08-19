from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.author_affiliations import crud
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


"""
Create a subroute /author_affiliations
"""
router = APIRouter(
    prefix="/author_affiliations",
    tags=["author_affiliations"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.AuthorAffiliation])
def get_author_affiliations(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
):
    return crud.get_author_affiliations(pagination, db)
