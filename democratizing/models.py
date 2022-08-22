from re import I
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Float,
    Integer,
    String,
    DateTime,
    Date,
)
from sqlalchemy.orm import relationship, declared_attr

from democratizing.database import Base


class DemocratizingModel(Base):
    """
    An abstract base model describing any table in the Democratizing Data DB
    """

    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    last_updated_date = Column(DateTime)


class DemocratizingRunModel(DemocratizingModel):
    """
    An abstract base model describing any table representing data generated by a run
    """

    __abstract__ = True

    @declared_attr
    def run_id(self):
        return Column(Integer, ForeignKey("agency_run.id"))


class DemocratizingExternalModel(Base):
    """
    An abstract mixin model describing any table generated by a run that also has an external ID
    """

    __abstract__ = True

    external_id = Column(String)


class Topic(DemocratizingRunModel):
    __tablename__ = "topic"

    keywords = Column(String)
    external_topic_id = Column(Integer)
    prominence = Column(Float)


class Publication(DemocratizingRunModel, DemocratizingExternalModel):
    __tablename__ = "publication"

    journal_id = Column(Integer)
    title = Column(String)
    doi = Column(String)
    year = Column(Integer)
    month = Column(Integer)
    pub_type = Column(String)
    citation_count = Column(Integer)
    fw_citation_impact = Column(Float)


class PublicationTopic(DemocratizingRunModel):
    __tablename__ = "publication_topic"

    publication_id = Column(Integer, ForeignKey("publication.id"))
    topic_id = Column(Integer, ForeignKey("topic.id"))
    score = Column(String)


class Author(DemocratizingRunModel, DemocratizingExternalModel):
    __tablename__ = "author"

    given_name = Column(String)
    family_name = Column(String)


class Model(DemocratizingModel):
    __tablename__ = "model"

    name = Column(String)
    github_commit_url = Column(String)
    description = Column(String)


class DatasetAlias(DemocratizingRunModel):
    __tablename__ = "dataset_alias"

    parent_alias_id = Column(Integer)
    alias_id = Column(Integer)
    alias = Column(String)
    alias_type = Column(String)
    url = Column(String)


class AgencyRun(DemocratizingModel):
    __tablename__ = "agency_run"

    agency = Column(String)
    version = Column(String)
    run_date = Column(DateTime)


class Affiliation(DemocratizingRunModel, DemocratizingExternalModel):
    __tablename__ = "affiliation"

    institution_name = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country_code = Column(String)
    postal_code = Column(String)


class Asjc(DemocratizingModel):
    __tablename__ = "asjc"

    code = Column(Integer)
    label = Column(String)


class Publisher(DemocratizingRunModel, DemocratizingExternalModel):
    __tablename__ = "publisher"

    name = Column(String)


class Journal(DemocratizingRunModel, DemocratizingExternalModel):
    __tablename__ = "journal"

    publisher_id = Column(Integer, ForeignKey("publisher.id"))
    title = Column(String)
    cite_score = Column(Float)


class DemocratizingPublicationIdModel(DemocratizingModel):
    """
    A mixin for publication ids
    """

    __abstract__ = True

    @declared_attr
    def publication_id(self):
        return Column(Integer, ForeignKey("publication.id"))


class PublicationAuthor(DemocratizingRunModel, DemocratizingPublicationIdModel):
    __tablename__ = "publication_author"

    author_id = Column(Integer, ForeignKey("author.id"))
    author_position = Column(Integer)


class PublicationAsjc(DemocratizingRunModel, DemocratizingPublicationIdModel):
    __tablename__ = "publication_asjc"

    asjc_id = Column(Integer, ForeignKey("asjc.id"))


class PublicationDatasetAlias(DemocratizingRunModel, DemocratizingPublicationIdModel):
    __tablename__ = "publication_dataset_alias"

    elsevier_id = Column(Integer)
    dataset_alias_id = Column(Integer, ForeignKey("dataset_alias.id"))
    alias_id = Column(Integer)
    mention_candidate = Column(String)
    snippet = Column(String)
    is_fuzzy = Column(Boolean)
    fuzzy_score = Column(Float)


class PdaModel(DemocratizingRunModel):
    __tablename__ = "pda_model"

    publication_dataset_alias_id = Column(
        Integer, ForeignKey("publication_dataset_alias.id")
    )
    model_id = Column(Integer, ForeignKey("model.id"))
    score = Column(Float)


class AuthorAffiliation(DemocratizingRunModel):
    __tablename__ = "author_affiliation"

    publication_author_id = Column(Integer, ForeignKey("publication_author.id"))
    affiliation_id = Column(Integer, ForeignKey("affiliation.id"))


class ISSN(DemocratizingRunModel):
    __tablename__ = "issn"

    journal_id = Column(Integer)
    ISSN = Column(String)
