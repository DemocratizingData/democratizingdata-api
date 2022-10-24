from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.publication_topics import crud
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


"""
Create a subroute /publication_topics
"""
router = APIRouter(
    prefix="/publication_topics",
    tags=["publication_topics"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.PublicationTopic])
def get_publication_topics(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
):
    return crud.get_publication_topics(pagination, db)
