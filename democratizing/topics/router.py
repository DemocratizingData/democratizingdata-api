from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.topics import crud
from sqlalchemy.orm import Session
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from typing import Union

logger = logging.getLogger(__name__)


"""
Create a subroute /topics
"""
router = APIRouter(
    prefix="/topics",
    tags=["topics"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.Topic])
def get_topics(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
    agency: Union[str, None] = None,
):
    return crud.get_topics(pagination, db, agency)


@router.get("/{topic_id}/publications", response_model=list[schemas.Publication])
def get_topic_publications(
    topic_id: int,
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
    agency: Union[str, None] = None,
):
    return crud.get_topic_publications(topic_id, pagination, db, agency)

@router.get("/{topic_id}/authors", response_model=list[schemas.Author])
def get_topic_authors(
        topic_id: int,
        pagination: PaginationParams = Depends(get_pagination_params),
        db: Session = Depends(get_db),
        agency: Union[str, None] = None,
):
    return crud.get_topic_authors(topic_id, pagination, db, agency)

@router.get("/{topic_id}/datasets", response_model=list[schemas.DatasetAlias])
def get_topic_datasets(
        topic_id: int,
        pagination: PaginationParams = Depends(get_pagination_params),
        db: Session = Depends(get_db),
        agency: Union[str, None] = None,
):
    return crud.get_topic_datasets(topic_id, pagination, db, agency)