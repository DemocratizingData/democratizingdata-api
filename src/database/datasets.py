from .database import engine
from .database import run_procedure
from .adapters import (
    create_publication,
    create_author,
    create_dataset,
    create_alias,
)
from .models import Topic, Publication, Author, Dataset, Alias
import logging

logger = logging.getLogger()


def create_topic_from_dataset(row: tuple[int, int, str, int, str]) -> Topic:
    return Topic(
        topic_id=row[0],
        keyword_id=row[1],
        keyword=row[2],
        source_id=row[3],
        organization_name=row[4],
    )


def get_datasets() -> list[Dataset]:
    return [create_dataset(row) for row in run_procedure("get_datasets", [])]


def get_dataset_aliases(parent_alias_id: int) -> list[Alias]:
    return [
        create_alias(row)
        for row in run_procedure("get_dataset_aliases", [parent_alias_id])
    ]


def get_dataset_publications(parent_alias_id: int) -> list[Publication]:
    return [
        create_publication(row)
        for row in run_procedure("get_dataset_publications", [parent_alias_id])
    ]


def get_dataset_topics(parent_alias_id: int) -> list[Topic]:
    return [
        create_topic_from_dataset(row)
        for row in run_procedure("get_dataset_topics", [parent_alias_id])
    ]


def get_dataset_authors(parent_alias_id: int) -> list[Dataset]:
    return [
        create_author(row)
        for row in run_procedure("get_dataset_authors", [parent_alias_id])
    ]
