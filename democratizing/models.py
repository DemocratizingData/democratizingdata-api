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
from sqlalchemy.orm import relationship

from democratizing.database import Base


class Topic(Base):
    __tablename__ = "topic"

    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer)
    keywords = Column(String)
    external_topic_id = Column(Integer)
    prominence = Column(Float)
    last_updated_date = Column(DateTime)


class Publication(Base):
    __tablename__ = "publication"

    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer)
    journal_id = Column(Integer)
    external_id = Column(String)
    title = Column(String)
    doi = Column(String)
    year = Column(Integer)
    month = Column(Integer)
    pub_type = Column(String)
    citation_count = Column(Integer)
    fw_citation_impact = Column(Float)
    last_updated_date = Column(DateTime)


class PublicationTopic(Base):
    __tablename__ = "publication_topic"

    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer)
    publication_id = Column(Integer, ForeignKey("publication.id"))
    topic_id = Column(Integer, ForeignKey("topic.id"))
    score = Column(String)
    last_updated_date = Column(DateTime)


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer)
    external_id = Column(String)
    given_name = Column(String)
    family_name = Column(String)
    last_updated_date = Column(String)


class Model(Base):
    __tablename__ = "model"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    github_commit_url = Column(String)
    description = Column(String)
    last_updated_date = Column(DateTime)


class DatasetAlias(Base):
    __tablename__ = "dataset_alias"

    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer)
    parent_alias_id = Column(Integer)
    alias_id = Column(Integer)
    alias = Column(String)
    alias_type = Column(String)
    url = Column(String)
    last_updated_date = Column(DateTime)


class AgencyRun(Base):
    __tablename__ = "agency_run"

    id = Column(Integer, primary_key=True, index=True)
    agency = Column(String)
    version = Column(String)
    run_date = Column(Date)
    last_updated_date = Column(DateTime)


class Affiliation(Base):
    __tablename__ = "affiliation"

    id = Column(Integer, primary_key=True, index=True)
    run_id = Column(Integer)
    external_id = Column(String)
    institution_name = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country_code = Column(String)
    postal_code = Column(String)
    last_updated_date = Column(DateTime)
