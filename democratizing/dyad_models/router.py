from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.dyad_models import crud
from sqlalchemy.orm import Session
from typing import Union

logger = logging.getLogger(__name__)


"""
Create a subroute /dyad_models
"""
router = APIRouter(
    prefix="/dyad_models",
    tags=["dyad_models"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.DyadModel])
def get_dyad_models(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
    agency: Union[str, None] = None,
):
    return crud.get_dyad_models(pagination, db, agency)
