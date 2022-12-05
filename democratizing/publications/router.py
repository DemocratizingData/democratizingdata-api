from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.publications import crud
from sqlalchemy.orm import Session
from typing import Union

logger = logging.getLogger(__name__)


"""
Create a subroute /publications
"""
router = APIRouter(
    prefix="/publications",
    tags=["publications"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.Publication])
def get_publications(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
    agency: Union[str, None] = None,
):
    return crud.get_publications(pagination, db, agency)

@router.get("/{publication_id}/topics", response_model=list[schemas.Topic])
def get_publication_topics(
    publication_id: int,
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
    agency: Union[str, None] = None,
):
    return crud.get_publication_topics(publication_id, pagination, db, agency)

@router.get("/{publication_id}/authors", response_model=list[schemas.Author])
def get_publication_authors(
    publication_id: int,
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
    agency: Union[str, None] = None,
):
    return crud.get_publication_authors(publication_id, pagination, db, agency)

@router.get("/{publication_id}/datasets", response_model=list[schemas.DatasetAlias])
def get_publication_datasets(
        publication_id: int,
        pagination: PaginationParams = Depends(get_pagination_params),
        db: Session = Depends(get_db),
        agency: Union[str, None] = None,
):
    return crud.get_publication_datasets(publication_id, pagination, db, agency)