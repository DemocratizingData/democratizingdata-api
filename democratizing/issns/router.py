from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.issns import crud
from sqlalchemy.orm import Session
from typing import Union

logger = logging.getLogger(__name__)


"""
Create a subroute /issns
"""
router = APIRouter(
    prefix="/issns",
    tags=["issns"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.ISSN])
def get_issns(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
    agency: Union[str, None] = None,
):
    return crud.get_issns(pagination, db, agency)
