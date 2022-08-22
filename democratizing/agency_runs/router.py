from fastapi import APIRouter, Depends
import logging
from democratizing import schemas
from democratizing.dependencies import get_db, get_pagination_params, PaginationParams
from democratizing.agency_runs import crud
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


"""
Create a subroute /agency_runs
"""
router = APIRouter(
    prefix="/agency_runs",
    tags=["agency_runs"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=list[schemas.AgencyRun])
def get_agency_runs(
    pagination: PaginationParams = Depends(get_pagination_params),
    db: Session = Depends(get_db),
):
    return crud.get_agency_runs(pagination, db)
