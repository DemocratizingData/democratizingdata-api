from fastapi import APIRouter, Depends
import logging
from democratizing import schemas, dependencies
from democratizing.topics import crud
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


"""
Create a subroute /topics
"""
router = APIRouter(
    prefix="/topics",
    tags=["topics"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.Topic])
def get_topics(
    limit: int | None = None,
    offset: int | None = None,
    db: Session = Depends(dependencies.get_db),
):
    return crud.get_topics(limit, offset, db)


@router.get("/{topic_id}/publications", response_model=list[schemas.Publication])
def get_topic_publications(
    topic_id: int,
    limit: int | None = None,
    offset: int | None = None,
    db: Session = Depends(dependencies.get_db),
):
    return crud.get_topic_publications(topic_id, limit, offset, db)
