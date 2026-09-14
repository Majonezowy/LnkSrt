from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class RedirectUrl(Base):
    __tablename__ = "redirecturls"

    id: Mapped[int] = mapped_column(primary_key=True)
    uid: Mapped[str] = mapped_column(String(16), unique=True)
    redirect_url: Mapped[str] = mapped_column(String(255))
