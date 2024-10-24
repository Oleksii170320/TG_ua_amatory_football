from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.services.region import get_regions_list
from app.services.tournament import get_football_types, get_tournaments_list


async def regions_list():
    all_regions = await get_regions_list()
    keyboard = InlineKeyboardBuilder()
    for region in all_regions:
        keyboard.add(InlineKeyboardButton(text=region.name, callback_data=f"region_{region.id}"))
    keyboard.add(InlineKeyboardButton(text='На головну', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def region_button(region_id):
    all_type = await get_football_types()
    keyboard = InlineKeyboardBuilder()
    for football_type in all_type:
        keyboard.add(InlineKeyboardButton(
            text=football_type.type,
            callback_data=f"type_{football_type.id}_region_{region_id}"
        ))
    keyboard.add(InlineKeyboardButton(text='На головну', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def region_tournaments(football_type_id, region_id):
    all_tournaments = await get_tournaments_list(football_type_id, region_id)
    keyboard = InlineKeyboardBuilder()
    for tournament in all_tournaments:
        keyboard.add(InlineKeyboardButton(text=tournament.name, url=f'{tournament.link}'))
    keyboard.add(InlineKeyboardButton(text='На головну', callback_data='to_main'))
    return keyboard.adjust(1).as_markup()
