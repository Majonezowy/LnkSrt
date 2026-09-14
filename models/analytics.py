from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import DateTime

from db.base import Base


class Analytics(Base):
    __tablename__ = "analytics"

    id: Mapped[int] = mapped_column(primary_key=True)
    alias: Mapped[str] = mapped_column(String(16))
    ip_address: Mapped[str] = mapped_column(String(15))
    referer: Mapped[str] = mapped_column(String(256))
    created_at: Mapped[datetime] = mapped_column(
            DateTime,
            server_default=func.now(),
            nullable=False,
        )
