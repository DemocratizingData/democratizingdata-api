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