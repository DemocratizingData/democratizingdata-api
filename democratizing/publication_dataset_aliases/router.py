from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.publication_dataset_aliases import crud
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


"""
Create a subroute /publication_dataset_aliases
"""
router = APIRouter(
    prefix="/publication_dataset_aliases",
    tags=["publication_dataset_aliases"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.PublicationDatasetAlias])
def get_publication_dataset_aliases(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
):
    return crud.get_publication_dataset_aliases(pagination, db)
