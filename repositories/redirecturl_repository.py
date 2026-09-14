from sqlalchemy import select
from sqlalchemy.orm import Session

from models.redirecturl import RedirectUrl


class RedirectUrlRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_uid(self, uid: str) -> RedirectUrl | None:
        stmt = select(RedirectUrl).where(RedirectUrl.uid == uid)

        return self.session.scalar(stmt)

    def create(self, uid: str, redirect_url: str) -> RedirectUrl:
        redirect = RedirectUrl(
            uid=uid,
            redirect_url=redirect_url,
        )

        self.session.add(redirect)
        self.session.commit()
        self.session.refresh(redirect)

        return redirect
