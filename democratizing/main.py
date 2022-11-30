from typing import Optional
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import os
import logging
import sys
from democratizing.routers import routers


# Set up logging
logger = logging.getLogger()
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
LOGLEVEL = os.environ.get("LOGLEVEL", "INFO")
SQL_LOGLEVEL = os.environ.get("SQL_LOGLEVEL", "INFO")
logger.setLevel(LOGLEVEL)
logging.getLogger("sqlalchemy.engine").setLevel(SQL_LOGLEVEL)

logger.error(f"Log level {LOGLEVEL}")
logger.error(f"SQLAlchemy Log Level {SQL_LOGLEVEL}")

# Initialize database
logger.debug("Initializing PostgreSQL connection")


tags_metadata = [
    {
        "name": "topics",
        "description": "Operations with topics",
    },
    {
        "name": "authors",
        "description": "Operations with authors",
    },
    {"name": "agency_runs", "description": "Operations with agency runs"},
    {"name": "dataset_aliases", "description": "Operations with dataset aliases"},
    {"name": "models", "description": "Operations with run models"},
    {"name": "datasets", "description": "Operations with datasets"},
    {"name": "publications", "description": "Operations with publications"},
    {"name": "asjcs", "description": "Operations with ASJCs"},
    {"name": "publishers", "description": "Operations with Publishers"},
    {"name": "journals", "description": "Operations with Journals"},
    {
        "name": "publication_authors",
        "description": "Operations with Publication Authors",
    },
    {"name": "publication_asjcs", "description": "Operations with Publication ASJCs"},
    {
        "name": "publication_dataset_aliases",
        "description": "Operations with Publication Dataset Aliases",
    },
    {"name": "pda_models", "description": "Operations with PDA Models"},
    {
        "name": "author_affiliations",
        "description": "Operations with Author Affiliations",
    },
    {"name": "issns", "description": "Operations with ISSNs"},
]


app = FastAPI(
    title="Democratizing Data API",
    description="An API for datasets",
    version="0.0.1",
    openapi_tags=tags_metadata,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include subroutes
for router in routers:
    app.include_router(router)
