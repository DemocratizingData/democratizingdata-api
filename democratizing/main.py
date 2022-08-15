from typing import Optional
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import os
import logging
import sys
from democratizing.topics.router import router as topics_router
from democratizing.publications.router import router as publications_router
from democratizing.run_models.router import router as models_router

# Set up logging
logger = logging.getLogger()
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
LOGLEVEL = os.environ.get("LOGLEVEL", "INFO")
logger.setLevel(LOGLEVEL)
logger.error(f"Log level {LOGLEVEL}")

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
    {"name": "models", "description": "Operations with run models"},
    {"name": "datasets", "description": "Operations with datasets"},
    {"name": "publications", "description": "Operations with publications"},
]


app = FastAPI(
    title="Show US the Data API",
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
app.include_router(topics_router)
app.include_router(publications_router)
app.include_router(models_router)
