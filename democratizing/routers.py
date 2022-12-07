from democratizing.topics.router import router as topics_router
from democratizing.publications.router import router as publications_router
from democratizing.run_models.router import router as models_router
from democratizing.authors.router import router as authors_router
from democratizing.dataset_aliases.router import router as dataset_aliases_router
from democratizing.agency_runs.router import router as agency_runs_router
from democratizing.publication_affiliations.router import router as publication_affiliations_router
from democratizing.datasets.router import router as datasets_router
from democratizing.asjcs.router import router as asjcs_router
from democratizing.publishers.router import router as publishers_router
from democratizing.journals.router import router as journals_router
from democratizing.publication_authors.router import router as publication_authors_router
from democratizing.publication_topics.router import router as publication_topics_router
from democratizing.publication_asjcs.router import router as publication_asjcs_router
from democratizing.dyads.router import router as dyads_router
from democratizing.dyad_models.router import router as dyad_models_router
from democratizing.author_affiliations.router import router as author_affiliations_router
from democratizing.issns.router import router as issns_router

routers = [
    topics_router,
    publications_router,
    models_router,
    authors_router,
    dataset_aliases_router,
    agency_runs_router,
    publication_affiliations_router,
    datasets_router,
    asjcs_router,
    publishers_router,
    journals_router,
    publication_topics_router,
    publication_authors_router,
    publication_asjcs_router,
    dyads_router,
    dyad_models_router,
    author_affiliations_router,
    issns_router,
]
