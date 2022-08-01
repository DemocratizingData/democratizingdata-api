from .models import Topic, Publication, Author, Dataset, Alias


def create_publication(row: tuple[int, str, str, int, int, str, int, float, str]):
    return Publication(
        publication_id=row[0],
        title=row[1],
        doi=row[2],
        year=row[3],
        month=row[4],
        pub_type=row[5],
        citation_count=row[6],
        fw_citation_impact=row[7],
        journal=row[8],
    )


def create_author(row: tuple[int, str, str]):
    return Author(author_id=row[0], given_name=row[1], family_name=row[2])


def create_dataset(row: tuple[int, str]):
    return Dataset(alias_id=row[0], alias=row[1])


def create_alias(row: tuple[int, str, str]):
    return Alias(alias_id=row[0], alias=row[1], alias_type=row[2])
