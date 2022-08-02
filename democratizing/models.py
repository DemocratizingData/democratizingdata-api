from sqlalchemy import Boolean, Column, ForeignKey, Float, Integer, String, DateTime
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
