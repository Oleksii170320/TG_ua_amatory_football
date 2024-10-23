from sqlalchemy import select

from app.core.database import async_session
from app.models.tournament import Tournament, Type


async def get_football_types():
    async with async_session() as session:
        return await session.scalars(select(Type))


async def get_football_type(type_id: int):
    async with async_session() as session:
        return await session.scalar(select(Type).where(Type.id == type_id))


async def get_tournaments_list(type_id, region_id):
    async with async_session() as session:
        return await session.scalars(select(Tournament).where(
            Tournament.type_id == type_id,
            Tournament.region_id == region_id)
        )


async def get_region_tournaments(region_id):
    async with async_session() as session:
        return await session.scalars(select(Tournament).where(Tournament.region_id == region_id))


async def get_tournament(tournament_id):
    async with async_session() as session:
        return await session.scalar(select(Tournament).where(Tournament.id == tournament_id))
