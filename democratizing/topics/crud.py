from democratizing.models import Topic
from sqlalchemy.orm import Session
import logging

logger = logging.getLogger()


def get_topics(db: Session):
    return db.query(Topic).all()


"""
def get_topic_publications(topic_id: int) -> list[Publication]:
    return [
        create_publication(row)
        for row in run_procedure("get_topic_publications", [topic_id])
    ]


def get_topic_authors(topic_id: int) -> list[Author]:
    return [
        create_author(row) for row in run_procedure("get_topic_authors", [topic_id])
    ]


def get_topic_datasets(topic_id: int) -> list[Dataset]:
    return [
        create_dataset(row) for row in run_procedure("get_topic_datasets", [topic_id])
    ]
"""
