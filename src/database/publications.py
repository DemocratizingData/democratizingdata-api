from .database import run_procedure
from .adapters import create_publication, create_author, create_dataset
from .models import Topic, Publication, Author, Dataset
import logging

logger = logging.getLogger()


def create_topic_from_publication(row: tuple[int, float, int, str, int, str]) -> Topic:
    return Topic(
        topic_id=row[0],
        score=row[1],
        keyword_id=row[2],
        keyword=row[3],
        source_id=row[4],
        organization_name=row[5],
    )


def get_publications() -> list[Publication]:
    return [create_publication(row) for row in run_procedure("get_publications", [])]


def get_publication_topics(publication_id: int) -> list[Topic]:
    return [
        create_topic_from_publication(row)
        for row in run_procedure("get_publication_topics", [publication_id])
    ]


def get_publication_authors(publication_id: int) -> list[Author]:
    return [
        create_author(row)
        for row in run_procedure("get_publication_authors", [publication_id])
    ]


def get_publication_datasets(publication_id: int) -> list[Dataset]:
    return [
        create_dataset(row)
        for row in run_procedure("get_publication_datasets", [publication_id])
    ]
