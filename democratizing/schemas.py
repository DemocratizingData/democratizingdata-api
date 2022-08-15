from datetime import datetime
from types import NoneType

from pydantic import BaseModel, Field, constr

from typing import Union
from enum import Enum


class Topic(BaseModel):
    """
    A searchable topic
    """

    id: int = Field(
        None,
        title="Topic ID",
        description="A unique ID that can be used to retrieve topics",
        example="32",
    )
    run_id: int = Field(
        None,
        title="Run ID",
        description="A unique ID that identifies which agency run generated this topic",
    )
    keywords: constr(max_length=1028) = Field(
        None,
        title="Keywords",
        description="A list of keywords separated by the pipe character |",
        example="Water Quality|Education",
    )
    external_topic_id: Union[constr(max_length=128), NoneType] = Field(
        None,
        title="External Topic ID",
        description="A unique ID that corresponds to an external topic",
    )
    prominence: Union[float, NoneType] = Field(
        None, title="Score", description="Relevance score"
    )
    last_updated_date: datetime = Field(
        None, title="Last Updated Date", description="Timestamp of last update"
    )

    class Config:
        orm_mode = True


class Publication(BaseModel):
    """
    A publication
    """

    id: int = Field(
        None,
        title="Publication ID",
        description="A unique ID that can be used to retrieve publications",
        example="366",
    )
    run_id: int = Field(
        None,
        title="Run ID",
        description="A unique ID that identifies which agency run generated this publication",
    )
    journal_id: int = Field(
        None,
        title="Journal ID",
        description="A unique ID that identified which journal has this publication",
    )
    external_id: constr(max_length=128) = Field(
        None,
        title="External ID",
        description="A unique ID that corresponds to an external identification for this publication",
    )
    title: constr(max_length=400) = Field(
        None,
        title="Title",
        description="The title of the article within the publication",
        example="Reintroducing the Current Insights Feature",
    )
    doi: constr(max_length=80) = Field(
        None,
        title="DOI",
        description="Digital Object Identifier",
        example="10.3386/w18780",
    )
    year: int = Field(
        None, title="Year", description="Year of the publication", example="2017"
    )
    month: int = Field(
        None, title="Month", description="Month of the publication", example="3"
    )
    pub_type: constr(max_length=30) = Field(
        None,
        title="Publication Type",
        description="Publication type",
        example="journal",
    )
    citation_count: int = Field(
        None,
        title="Citation Count",
        description="The number of citations for this publication",
        example="5",
    )
    fw_citation_impact: float = Field(
        None, title="Citation Impact", description="The impact of this citation (DRAFT)"
    )

    class Config:
        orm_mode = True


class Author(BaseModel):
    """
    An author
    """

    id: int = Field(
        None,
        title="Author",
        description="The unique ID of an author",
    )
    external_d: Union[constr(max_length=128), NoneType] = Field(
        None,
        title="External ID",
        description="A unique external ID for this author",
    )
    given_name: constr(max_length=150) = Field(
        None, title="Given Name", description="The author's given name"
    )
    family_name: constr(max_length=150) = Field(
        None, title="Family Name", description="The author's familiy name"
    )
    last_updated_date: datetime = Field(
        None, title="Last Updated Date", description="Timestamp of last update"
    )

    class Config:
        orm_mode = True


class DatasetAlias(BaseModel):
    """
    A dataset alias
    """

    id: int = Field(
        None,
        title="Dataset ID",
        description="The unique ID of this dataset record. For joins to other schema, please use alias_id",
    )
    run_id: int = Field(
        None,
        title="Run ID",
        description="A unique ID that identifies which agency run generated this dataset",
    )
    alias_id: int = Field(
        None,
        title="Alias ID",
        description="The alias ID of a dataset, for identifying this dataset's usage in other tables",
    )
    alias: constr(max_length=160) = Field(
        None, title="Alias", description="The identifying alias or name of a dataset"
    )
    alias_type: constr(max_length=50) = Field(
        None, title="Alias Type", description="The type of alias for this dataset"
    )
    url: constr(max_length=2048) = Field(
        None, title="URL", description="The URL for retrieving this dataset"
    )
    last_updated_date: datetime = Field(
        None, title="Last Updated Date", description="Timestamp of last update"
    )

    class Config:
        orm_mode = True


class Model(BaseModel):
    """
    A run model
    """

    id: int = Field(
        None, title="Model ID", description="A unique ID that identifies this model"
    )
    name: constr(max_length=32) = Field(
        None, title="Name", description="The name of this model"
    )
    github_commit_url: constr(max_length=1024) = Field(
        None,
        title="Github Commit URL",
        description="The URL for the GitHub commit that contains this model",
    )
    description: constr(max_length=2048) = Field(
        None, title="Description", description="A short description of this model"
    )
    last_updated_date: datetime = Field(
        None, title="Last Updated Date", description="Timestamp of last update"
    )

    class Config:
        orm_mode = True
