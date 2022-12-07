from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.pda_models import crud
from sqlalchemy.orm import Session
from typing import Union

logger = logging.getLogger(__name__)


"""
Create a subroute /pda_models
"""
router = APIRouter(
    prefix="/pda_models",
    tags=["pda_models"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.PdaModel])
def get_pda_models(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
    agency: Union[str, None] = None,
):
    return crud.get_pda_models(pagination, db, agency)
