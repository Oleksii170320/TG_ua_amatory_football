from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb
import app.services.requests as rq

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer('Ласкаво просимо до каналу Аматорського футболу та футзалу в України та її регіонах!', reply_markup=kb.main)


@router.message(F.text == 'Список областей')
async def reg_list(message: Message):
    await message.answer('Виберіть необхідну область', reply_markup=await kb.regions_list())


# @router.callback_query(F.data.startswith('region_'))
# async def category(callback: CallbackQuery):
#     await callback.message.answer(f'Виберіть турнір {callback.data}',
#                                   reply_markup=await kb.items(callback.data.split('_')[1]))


@router.callback_query(F.data.startswith('region_'))
async def reg_item(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.message.answer(f'Ви обрали {item_data.region_name} область\n'
                                  f'Офіційний футбольний сайт: {item_data.football_link}\n'
                                  f'Офіційний футзальний сайт: {item_data.futsal_link}')