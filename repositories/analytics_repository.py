from sqlalchemy import func, select
from sqlalchemy.orm import Session

from models.analytics import Analytics


class AnalyticsRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_alias(self, alias: str) -> Analytics | None:
        stmt = select(Analytics).where(Analytics.alias == alias)

        return self.session.scalar(stmt)

    def number_of_clicks(self, alias: str) -> int:
        stmt = (
            select(func.count())
            .select_from(Analytics)
            .where(Analytics.alias == alias)
        )

        return self.session.scalar(stmt) or 0

    def get_n_stats(self, alias: str, limit: int) -> list[Analytics]:
        stmt = (
            select(Analytics)
            .where(Analytics.alias == alias)
            .order_by(Analytics.created_at.desc())
            .limit(limit)
        )

        return list(self.session.scalars(stmt).all())

    def create(self, alias: str, ip_address: str, referer: str) -> Analytics:
        redirect = Analytics(
            alias=alias,
            ip_address=ip_address,
            referer=referer,
        )

        self.session.add(redirect)
        self.session.commit()
        self.session.refresh(redirect)

        return redirect
