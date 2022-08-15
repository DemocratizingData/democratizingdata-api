from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.dataset_aliases import crud
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


"""
Create a subroute /dataset_aliases
"""
router = APIRouter(
    prefix="/dataset_aliases",
    tags=["dataset_aliases"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.DatasetAlias])
def get_dataset_aliases(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
):
    return crud.get_dataset_aliases(pagination, db)
