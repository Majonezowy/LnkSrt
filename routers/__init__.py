from fastapi import APIRouter

from .analytics import router as analytics_router
from .rediect import router as redirect_router

router = APIRouter()

router.include_router(redirect_router)
router.include_router(analytics_router)
