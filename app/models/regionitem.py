from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class RegionItem(Base):
    __tablename__ = 'regionitems'

    id: Mapped[int] = mapped_column(primary_key=True)
    region_name: Mapped[str] = mapped_column(String(120))
    football_link: Mapped[str] = mapped_column(String(120), nullable=True)
    futsal_link: Mapped[str] = mapped_column(String(120), nullable=True)
    region_id: Mapped[int] = mapped_column(ForeignKey('regions.id'))


