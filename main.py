from fastapi import FastAPI

from db.base import Base
from db.database import engine
from middleware.analytics import log_requests_middleware
from routers import router

app = FastAPI()

#middleware
app.middleware("http")(log_requests_middleware)

#init db
Base.metadata.create_all(engine)

#include all routers
app.include_router(router=router)
