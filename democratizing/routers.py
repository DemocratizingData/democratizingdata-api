from democratizing.topics.router import router as topics_router
from democratizing.publications.router import router as publications_router
from democratizing.run_models.router import router as models_router
from democratizing.authors.router import router as authors_router

routers = [
    topics_router,
    publications_router,
    models_router,
    authors_router
]
