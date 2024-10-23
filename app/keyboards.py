from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.services.requests import get_region_item, get_regions_list

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Список областей')],
                                     [KeyboardButton(text='Контакти'),
                                      KeyboardButton(text='Про нас')]],
                           resize_keyboard=True,
                           input_field_placeholder='Виберіть пункт меню...')


async def regions_list():
    all_regions = await get_regions_list()
    keyboard = InlineKeyboardBuilder()
    for region in all_regions:
        keyboard.add(InlineKeyboardButton(text=region.name, callback_data=f"region_{region.id}"))
    keyboard.add(InlineKeyboardButton(text='На головну', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()


async def items(region_id):
    all_items = await get_region_item(region_id)
    keyboard = InlineKeyboardBuilder()
    for item in all_items:
        keyboard.add(InlineKeyboardButton(text=f'Ви обрали {item.region_name} бласть,\nОфіційниф сайт футболу: {item.link},', callback_data=f"item_{item.id}"))
    keyboard.add(InlineKeyboardButton(text='На головну', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()