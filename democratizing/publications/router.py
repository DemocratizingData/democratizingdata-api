from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.publications import crud
from sqlalchemy.orm import Session

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
):
    return crud.get_publications(pagination, db)
