from datetime import datetime
from types import NoneType

from pydantic import BaseModel, Field
from typing import Union
from enum import Enum


class Topic(BaseModel):
    """
    A searchable topic
    """

    topic_id: int = Field(
        None,
        title="Topic ID",
        description="A unique ID that can be used to retrieve topics",
        example="32",
    )
    keyword_id: int = Field(
        None,
        title="Keyword ID",
        description="A unique ID that can be used to retrieve the keyword for a topic",
        example="1",
    )
    keyword: str = Field(
        None,
        title="Keyword",
        description="The keyword for a topic",
        example="Water Quality",
    )
    score: Union[float, NoneType] = Field(
        None, title="Score", description="Relevance score"
    )
    source_id: Union[int, NoneType] = Field(
        None,
        title="Source ID",
        description="A unique ID identifying the metadata source",
    )
    organization_name: Union[str, NoneType] = Field(
        None, title="Organization Name", description="An organization name"
    )


class Publication(BaseModel):
    """
    A publication
    """

    publication_id: int = Field(
        None,
        title="Publication ID",
        description="A unique ID that can be used to retrieve publications",
        example="366",
    )
    title: str = Field(
        None,
        title="Title",
        description="The title of the article within the publication",
        example="Reintroducing the Current Insights Feature",
    )
    doi: str = Field(
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
    pub_type: str = Field(
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
    journal: str = Field(
        None, title="Journal", description="The name of the publication"
    )


class Author(BaseModel):
    """
    An author
    """

    author_id: int = Field(
        None,
        title="Author",
        description="The unique ID of an author",
    )
    given_name: str = Field(
        None, title="Given Name", description="The author's given name"
    )
    family_name: str = Field(
        None, title="Family Name", description="The author's familiy name"
    )


class Dataset(BaseModel):
    """
    A dataset
    """

    alias_id: int = Field(
        None, title="Dataset ID", description="The unique ID of a dataset"
    )
    alias: str = Field(
        None, title="Alias", description="The identifying alias or name of a dataset"
    )


class AliasType(str, Enum):
    alias = "alias"
    main = "main"


class Alias(BaseModel):
    """
    A dataset alias
    """

    alias_id: int = Field(
        None, title="Alias ID", description="A unique ID that corresponds to an alias"
    )
    alias: str = Field(None, title="Alias", description="The name of a dataset alias")
    alias_type: AliasType = Field(
        None, title="Alias Type", description="The type of alias. This can be "
    )
