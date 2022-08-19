from datetime import datetime
from types import NoneType

from pydantic import BaseModel, Field, constr

from typing import Union
from enum import Enum


class DemocratizingSchema(BaseModel):
    """
    A basemodel for all schemas
    """

    id: int = Field(
        None,
        title="ID",
        description="A unique ID for this row",
        example="32",
    )
    last_updated_date: datetime = Field(
        None, title="Last Updated Date", description="Timestamp of last update"
    )

    class Config:
        orm_mode = True


class DemocratizingRunSchema(DemocratizingSchema):
    """
    A basemodel for those schemas with a run_id field
    """

    run_id: int = Field(
        None,
        title="Run ID",
        description="A unique ID that identifies which agency run generated this row",
    )


class DemocratizingExternalSchema(BaseModel):
    """
    A mixin for schemas that have an external_id field
    """

    external_id: Union[constr(max_length=128), NoneType] = Field(
        None,
        title="External ID",
        description="An ID for identifying this record in an external data source",
    )


class Topic(DemocratizingRunSchema):
    """
    A searchable topic
    """

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


class Publication(DemocratizingRunSchema, DemocratizingExternalSchema):
    """
    A publication
    """

    journal_id: int = Field(
        None,
        title="Journal ID",
        description="A unique ID that identified which journal has this publication",
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


class Author(DemocratizingRunSchema, DemocratizingExternalSchema):
    """
    An author
    """

    given_name: constr(max_length=150) = Field(
        None, title="Given Name", description="The author's given name"
    )
    family_name: constr(max_length=150) = Field(
        None, title="Family Name", description="The author's familiy name"
    )


class DatasetAlias(DemocratizingRunSchema):
    """
    A dataset alias
    """

    alias_id: int = Field(
        None,
        title="Alias ID",
        description="The alias ID of a dataset, for identifying this dataset's usage in other tables",
    )
    alias: Union[constr(max_length=160), NoneType] = Field(
        None, title="Alias", description="The identifying alias or name of a dataset"
    )
    parent_alias_id: Union[int, NoneType] = Field(
        None,
        title="Parent Alias ID",
        description="If this dataset alias is a child, the parent_alias_id field identifies the parent alias",
    )
    alias_type: Union[constr(max_length=50), NoneType] = Field(
        None, title="Alias Type", description="The type of alias for this dataset"
    )
    url: Union[constr(max_length=2048), NoneType] = Field(
        None, title="URL", description="The URL for retrieving this dataset"
    )


class Model(DemocratizingSchema):
    """
    A run model
    """

    name: constr(max_length=32) = Field(
        None, title="Name", description="The name of this model"
    )
    github_commit_url: Union[constr(max_length=1024), NoneType] = Field(
        None,
        title="Github Commit URL",
        description="The URL for the GitHub commit that contains this model",
    )
    description: Union[constr(max_length=2048), NoneType] = Field(
        None, title="Description", description="A short description of this model"
    )


class AgencyRun(DemocratizingSchema):
    """
    An agency run
    """

    agency: constr(max_length=32) = Field(
        None, title="Agency", description="The name of the agency for this run"
    )
    version: constr(max_length=32) = Field(
        None, title="Version", description="The version number for this run"
    )
    run_date: Union[datetime, NoneType] = Field(
        None, title="Run Date", description="The date of this run"
    )


class Affiliation(DemocratizingRunSchema, DemocratizingExternalSchema):
    """
    Institution affiliations
    """

    institution_name: Union[constr(max_length=750), NoneType] = Field(
        None,
        title="Institution Name",
        description="The name of the institution of this affiliation",
    )
    address: Union[constr(max_length=750), NoneType] = Field(
        None, title="Address", description="The street address of this affiliation"
    )
    city: Union[constr(max_length=128), NoneType] = Field(
        None, title="City", description="The name of the city of this affiliation"
    )
    state: Union[constr(max_length=128), NoneType] = Field(
        None, title="State", description="The state of this affiliation"
    )
    country_code: Union[constr(max_length=10), NoneType] = Field(
        None, title="Country Code", description="The country code of this affiliation"
    )
    postal_code: Union[constr(max_length=32), NoneType] = Field(
        None, title="Postal Code", description="The postal code of this affiliation"
    )


class Dataset(DatasetAlias, AgencyRun):
    pass


class Asjc(DemocratizingRunSchema):
    code: int = Field(None, title="Code", description="ASJC Code")
    label: Union[constr(max_length=1024), NoneType] = Field(
        None, title="Label", description="A label for this ASJC"
    )


class Publisher(DemocratizingRunSchema, DemocratizingExternalSchema):
    name: Union[constr(max_length=120), NoneType] = Field(
        None, title="Publisher", description="The name of a publisher"
    )
