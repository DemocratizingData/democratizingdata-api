from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.full_authors import crud
from sqlalchemy.orm import Session
from typing import Union

logger = logging.getLogger(__name__)

"""
Create a subroute /full-authors
"""
router = APIRouter(
    prefix="/full_authors",
    tags=["full_authors"],
    responses={404: {"description": "Not found"}},
)

@router.get("", response_model=list[schemas.FullAuthor])
def get_full_authors(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
    agency: Union[str, None] = None,
):
    return crud.get_full_authors(pagination, db, agency)