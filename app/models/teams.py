from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Team(Base):
    __tablename__ = 'teams'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    city: Mapped[str] = mapped_column(String(30), nullable=True)
    region_id: Mapped[int] = mapped_column(ForeignKey('regions.id'))
    logo: Mapped[str] = mapped_column(String(120), nullable=True)
