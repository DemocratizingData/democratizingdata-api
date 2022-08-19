from democratizing.topics.router import router as topics_router
from democratizing.publications.router import router as publications_router
from democratizing.run_models.router import router as models_router
from democratizing.authors.router import router as authors_router
from democratizing.dataset_aliases.router import router as dataset_aliases_router
from democratizing.agency_runs.router import router as agency_runs_router
from democratizing.affiliations.router import router as affiliations_router
from democratizing.datasets.router import router as datasets_router
from democratizing.asjcs.router import router as asjcs_router
from democratizing.publishers.router import router as publishers_router
from democratizing.journals.router import router as journals_router
from democratizing.publication_authors.router import (
    router as publication_authors_router,
)
from democratizing.publication_asjcs.router import router as publication_asjcs_router
from democratizing.publication_dataset_aliases.router import (
    router as publication_dataset_aliases_router,
)

routers = [
    topics_router,
    publications_router,
    models_router,
    authors_router,
    dataset_aliases_router,
    agency_runs_router,
    affiliations_router,
    datasets_router,
    asjcs_router,
    publishers_router,
    journals_router,
    publication_authors_router,
    publication_asjcs_router,
    publication_dataset_aliases_router,
]
