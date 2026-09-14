from fastapi.routing import APIRouter
from pydantic import BaseModel

from db.database import SessionLocal
from repositories.analytics_repository import AnalyticsRepository

router = APIRouter(prefix="/analytics")

class NumberOfClicksModel(BaseModel):
    alias: str

@router.post("/clicks")
async def get_number_of_clicks(data: NumberOfClicksModel):
    alias = data.alias

    with SessionLocal() as session:
        repo = AnalyticsRepository(session)

        number_of_clicks = repo.number_of_clicks(alias=alias)

        return number_of_clicks

class RedirectStatsModel(BaseModel):
    alias: str
    limit: int = 50

@router.post("/stats")
async def get_redirect_stats(data: RedirectStatsModel):
    alias = data.alias
    limit = data.limit

    with SessionLocal() as session:
        repo = AnalyticsRepository(session)

        stats = repo.get_n_stats(alias, limit)

        return stats
