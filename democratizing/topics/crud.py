from democratizing.models import Topic, Publication, PublicationTopic
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_topics(db: Session):
    return db.query(Topic).all()


def get_topic_publications(topic_id: int, db: Session):
    return (
        db.query(Publication)
        .join(PublicationTopic)
        .filter(PublicationTopic.topic_id == topic_id)
        .all()
    )
