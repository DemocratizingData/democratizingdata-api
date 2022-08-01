from .database import run_procedure
from .adapters import create_publication, create_author, create_dataset
from .models import Topic, Publication, Author, Dataset
import logging

logger = logging.getLogger()


def create_topic_from_listing(row: tuple[int, int, str]) -> Topic:
    return Topic(topic_id=row[0], keyword_id=row[1], keyword=row[2])


def get_topics() -> list[Topic]:
    return [create_topic_from_listing(row) for row in run_procedure("get_topics", [])]


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
