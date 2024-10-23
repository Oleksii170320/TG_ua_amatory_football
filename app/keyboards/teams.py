from aiogram.types import InlineKeyboardButton

from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.services.team import get_team


# async def region_teams(region_id):
#     all_teams = await get_teams(region_id)
#     keyboard = InlineKeyboardBuilder()
#     for team in all_teams:
#         keyboard.add(InlineKeyboardButton(text=f'{team.name} ({team.city})', callback_data=f"team_{team.id}"))
#     keyboard.add(InlineKeyboardButton(text='На головну', callback_data='to_main'))
#     return keyboard.adjust(1).as_markup()


async def team(team_id):
    iteam = await get_team(team_id)
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text=f'Ви обрали {iteam.name} ({iteam.city})'))
    keyboard.add(InlineKeyboardButton(text='На головну', callback_data='to_main'))
    return keyboard.adjust(2).as_markup()
