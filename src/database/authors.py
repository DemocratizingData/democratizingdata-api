from .database import engine
from .database import run_procedure
from .adapters import create_publication, create_author, create_dataset
from .models import Topic, Publication, Author, Dataset
import logging

logger = logging.getLogger()


def create_topic_from_author(row: tuple[int, int, str, int, str]) -> Topic:
    return Topic(
        topic_id=row[0],
        keyword_id=row[1],
        keyword=row[2],
        source_id=row[3],
        organization_name=row[4],
    )


def get_authors() -> list[Author]:
    return [create_author(row) for row in run_procedure("get_authors", [])]


def get_author_publications(author_id: int) -> list[Publication]:
    return [
        create_publication(row)
        for row in run_procedure("get_author_publications", [author_id])
    ]


def get_author_topics(author_id: int) -> list[Topic]:
    return [
        create_topic_from_author(row)
        for row in run_procedure("get_author_topics", [author_id])
    ]


def get_author_datasets(author_id: int) -> list[Dataset]:
    return [
        create_dataset(row) for row in run_procedure("get_author_datasets", [author_id])
    ]
