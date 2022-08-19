from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.publication_asjcs import crud
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


"""
Create a subroute /publication_asjcs
"""
router = APIRouter(
    prefix="/publication_asjcs",
    tags=["publication_asjcs"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.PublicationAsjc])
def get_publication_asjcs(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
):
    return crud.get_publication_asjcs(pagination, db)
