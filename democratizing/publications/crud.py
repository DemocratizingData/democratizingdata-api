from democratizing.models import Publication
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_publications(db: Session):
    return db.query(Publication).all()
