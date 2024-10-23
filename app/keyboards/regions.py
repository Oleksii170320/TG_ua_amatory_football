from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.services.region import get_regions_list, get_region_item
from app.services.tournament import get_football_types


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
