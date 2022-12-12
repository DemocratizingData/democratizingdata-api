"""
Create a subroute /full-authors
"""
router = APIRouter(
    prefix="/full_authors",
    tags=["full_authors"],
    responses={404: {"description": "Not found"}},
)
