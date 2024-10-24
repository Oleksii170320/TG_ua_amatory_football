from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards.teams as kb
from app.keyboards import regions as kb_region
from app.services.region import get_item, get_region
from app.services.tournament import get_tournaments_list, get_football_type
from app.services.user import set_user
from app.keyboards import main as kb_main

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(message.from_user.id)
    await message.answer('Ласкаво просимо до каналу Аматорського футболу та футзалу в України та її регіонах!', reply_markup=kb_main.main)


@router.message(F.text == 'Список областей')
async def reg_list(message: Message):
    await message.answer('Виберіть необхідну область', reply_markup=await kb_region.regions_list())


@router.message(F.text == 'Контакти')
async def reg_list(message: Message):
    await message.answer('Адреса: м. Київ, вул ******* 17\n'
                         'тел: +38-0**-***-**-88', reply_markup=kb_main.main)


@router.message(F.text == 'Про нас')
async def reg_list(message: Message):
    await message.answer('Колектив любителів статистики аматорського футболу та футзалу України',
                         reply_markup=kb_main.main)


@router.callback_query(F.data == 'to_main')
async def go_to_main(message: Message):
    await set_user(message.from_user.id)
    await message.answer('Ласкаво просимо до каналу Аматорського футболу та футзалу в України та її регіонах!',
                         reply_markup=kb_main.main)


@router.callback_query(F.data.startswith('region_'))
async def reg_item(callback: CallbackQuery):
    item_data = await get_item(callback.data.split('_')[1])
    await callback.message.answer(f'Ви обрали {item_data.region_name} область\n'
                                  f'Офіційний футбольний сайт: {item_data.football_link}\n'
                                  f'Офіційний футзальний сайт: {item_data.futsal_link}')
    await callback.message.answer(f'Оберіть футбол чи футзал:',
                                  reply_markup=await kb_region.region_button(callback.data.split('_')[1]))


def transform_region_name_to_locative(region_name: str) -> str:
    if region_name.endswith("ка"):
        return region_name[:-2] + "кій області"
    elif region_name.endswith("їв"):
        return region_name[:-2] + "єві"


def transform_football_type(type_name: str) -> str:
    if type_name.endswith("л"):
        return type_name[:] + "у"


@router.callback_query(F.data.startswith('type_'))
async def get_reg_type(callback: CallbackQuery):
    data_parts = callback.data.split('_')
    if len(data_parts) >= 4 and data_parts[0] == 'type' and data_parts[2] == 'region':
        football_type_id = int(data_parts[1])
        region_id = int(data_parts[3])

        # Отримання списку турнірів з використанням football_type_id та region_id
        region = await get_region(region_id)
        region_name = transform_region_name_to_locative(region.name).upper()
        football_type = await get_football_type(football_type_id)
        football_type_name = transform_football_type(football_type.type).upper()

        await callback.message.answer(
            f'Всі турніри {football_type_name} в {region_name}:',
                                  reply_markup=await kb_region.region_tournaments(football_type_id, region_id))
