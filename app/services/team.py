from app.core.database import async_session
from sqlalchemy import select

from app.models.teams import Team


async def get_teams(region_id):
    async with async_session() as session:
        return await session.scalars(select(Team).where(Team.region_id == region_id))


async def get_team(team_id):
    async with async_session() as session:
        return await session.scalars(select(Team).where(Team.id == team_id))
