from democratizing.database import SessionLocal
from pydantic import BaseModel


class PaginationParams(BaseModel):
    limit: int | None
    offset: int | None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_pagination_params(
    limit: int | None = None, offset: int | None = None
) -> PaginationParams:
    return PaginationParams(limit=limit, offset=offset)
