from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Type(Base):
    __tablename__ = 'types'

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(20), nullable=False)


class Tournament(Base):
    __tablename__ = 'tournaments'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    logo: Mapped[str] = mapped_column(String(120), nullable=True)
    link: Mapped[str] = mapped_column(String(120), nullable=True)
    region_id: Mapped[int] = mapped_column(ForeignKey('regions.id'))
    type_id: Mapped[int] = mapped_column(ForeignKey('types.id'))
