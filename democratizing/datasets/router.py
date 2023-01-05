from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.datasets import crud
from sqlalchemy.orm import Session
from typing import Union

logger = logging.getLogger(__name__)


"""
Create a subroute /datasets
"""
router = APIRouter(
    prefix="/datasets",
    tags=["datasets"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.Dataset])
def get_datasets(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
    agency: Union[str, None] = None,
):
    return crud.get_datasets(pagination, db, agency)

@router.get("/{parent_alias_id}/topics", response_model=list[schemas.Topic])
def get_publication_topics(
    parent_alias_id: int,
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
    agency: Union[str, None] = None,
):
    return crud.get_dataset_topics(parent_alias_id, pagination, db, agency)

@router.get("/{parent_alias_id}/authors", response_model=list[schemas.FullAuthor])
def get_publication_authors(
    parent_alias_id: int,
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
    agency: Union[str, None] = None,
):
    return crud.get_dataset_authors(parent_alias_id, pagination, db, agency)

@router.get("/{parent_alias_id}/publications", response_model=list[schemas.Publication])
def get_publication_datasets(
        parent_alias_id: int,
        pagination: PaginationParams = Depends(get_pagination_params),
        db: Session = Depends(get_db),
        agency: Union[str, None] = None,
):
    return crud.get_dataset_publications(parent_alias_id, pagination, db, agency)

@router.get("/{parent_alias_id}/aliases", response_model=list[schemas.DatasetAlias])
def get_publication_datasets(
        parent_alias_id: int,
        pagination: PaginationParams = Depends(get_pagination_params),
        db: Session = Depends(get_db),
        agency: Union[str, None] = None,
):
    return crud.get_dataset_aliases(parent_alias_id, pagination, db, agency)