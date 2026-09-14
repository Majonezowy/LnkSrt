from fastapi import Depends, Request
from fastapi.responses import RedirectResponse, Response
from fastapi.routing import APIRouter
from pydantic import BaseModel

from db.database import SessionLocal
from repositories.analytics_repository import AnalyticsRepository
from repositories.redirecturl_repository import RedirectUrlRepository

router = APIRouter()

async def track_shortlink(request: Request):
    alias = request.path_params["alias"]

    print({
        "alias": alias,
        "ip": request.client.host if request.client else None,
        "user_agent": request.headers.get("user-agent"),
        "referer": request.headers.get("referer"),
    })

    with SessionLocal() as session:
        repo = AnalyticsRepository(session)

        repo.create(
            alias=alias,
            ip_address=request.client.host if request.client else "",
            referer=request.headers.get("referer", "")
        )


@router.get(
    "/{alias}",
    dependencies=[Depends(track_shortlink)],
)
async def redirect(alias: str):
    with SessionLocal() as session:
        repo = RedirectUrlRepository(session)

        redirect_url = repo.get_by_uid(alias)

        if not redirect_url:
            return Response(status_code=404)

        return RedirectResponse(redirect_url.redirect_url)


class CreateRedirectUrlModel(BaseModel):
    alias: str
    redirect_url: str

@router.post(
    "/create",
)
async def create_redirect_url(data: CreateRedirectUrlModel):
    with SessionLocal() as session:
        repo = RedirectUrlRepository(session)

        redirect = repo.create(
            uid=data.alias,
            redirect_url=data.redirect_url,
        )

        return redirect
