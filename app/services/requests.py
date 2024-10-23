from app.core.database import async_session
from sqlalchemy import select


from app.models.regionitem import RegionItem
from app.models.region import Region
from app.models.user import User


async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()


async def get_regions_list():
    async with async_session() as session:
        return await session.scalars(select(Region))


async def get_region_item(region_id):
    async with async_session() as session:
        return await session.scalars(select(RegionItem).where(RegionItem.region_id == region_id))


async def get_item(item_id):
    async with async_session() as session:
        return await session.scalar(select(RegionItem).where(RegionItem.id == item_id))