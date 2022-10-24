from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.authors import crud
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


"""
Create a subroute /authors
"""
router = APIRouter(
    prefix="/authors",
    tags=["authors"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.Author])
def get_authors(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
):
    return crud.get_authors(pagination, db)

@router.get("/{author_id}/topics", response_model=list[schemas.Topic])
def get_publication_topics(
    author_id: int,
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
):
    return crud.get_author_topics(author_id, pagination, db)

@router.get("/{author_id}/publications", response_model=list[schemas.Publication])
def get_publication_authors(
    author_id: int,
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
):
    return crud.get_author_publications(author_id, pagination, db)

@router.get("/{author_id}/datasets", response_model=list[schemas.DatasetAlias])
def get_publication_datasets(
        author_id: int,
        pagination: PaginationParams = Depends(get_pagination_params),
        db: Session = Depends(get_db),
):
    return crud.get_author_datasets(author_id, pagination, db)