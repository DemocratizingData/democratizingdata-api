from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.publishers import crud
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


"""
Create a subroute /publishers
"""
router = APIRouter(
    prefix="/publishers",
    tags=["publishers"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.Publisher])
def get_publishers(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
):
    return crud.get_publishers(pagination, db)
