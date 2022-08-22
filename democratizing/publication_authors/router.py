from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.publication_authors import crud
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


"""
Create a subroute /publication_authors
"""
router = APIRouter(
    prefix="/publication_authors",
    tags=["publication_authors"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.PublicationAuthor])
def get_publication_authors(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
):
    return crud.get_publication_authors(pagination, db)
