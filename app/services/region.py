from app.core.database import async_session
from sqlalchemy import select

from app.models.region import Region
from app.models.regionitem import RegionItem


async def get_region(region_id):
    async with async_session() as session:
        return await session.scalar(select(Region).where(Region.id == region_id))


async def get_regions_list():
    async with async_session() as session:
        return await session.scalars(select(Region))


async def get_region_item(region_id):
    async with async_session() as session:
        return await session.scalars(select(RegionItem).where(RegionItem.region_id == region_id))

async def get_item(item_id):
    async with async_session() as session:
        return await session.scalar(select(RegionItem).where(RegionItem.id == item_id))