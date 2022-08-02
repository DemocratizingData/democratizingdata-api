from fastapi import APIRouter, Depends
import logging
from democratizing import schemas, dependencies
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
def get_publications(db: Session = Depends(dependencies.get_db)):
    return crud.get_publications(db)
