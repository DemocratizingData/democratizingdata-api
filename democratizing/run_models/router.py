from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.run_models import crud
from sqlalchemy.orm import Session
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from typing import Union

logger = logging.getLogger(__name__)


"""
Create a subroute /models
"""
router = APIRouter(
    prefix="/models",
    tags=["models"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.Model])
def get_models(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
    agency: Union[str, None] = None,
):
    return crud.get_models(pagination, db, agency)
