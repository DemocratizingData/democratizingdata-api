from democratizing.models import Topic, Publication, PublicationTopic
from sqlalchemy.orm import Session
from democratizing.utils import apply_limit_offset
import logging

logger = logging.getLogger()


def get_topics(limit: int | None, offset: int | None, db: Session):
    return apply_limit_offset(db.query(Topic), limit, offset).all()


def get_topic_publications(
    topic_id: int, limit: int | None, offset: int | None, db: Session
):
    return apply_limit_offset(
        db.query(Publication)
        .join(PublicationTopic)
        .filter(PublicationTopic.topic_id == topic_id),
        limit,
        offset,
    ).all()
