from democratizing.publications.crud import get_publications
from democratizing.schemas import Publication


def test_get_topics(integration_db_session, publication_schema):
    result = Publication.from_orm(get_publications(1, 0, integration_db_session)[0])
    assert result == publication_schema
