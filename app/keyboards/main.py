from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Список областей')],
                                     [KeyboardButton(text='Контакти'),
                                      KeyboardButton(text='Про нас')]],
                           resize_keyboard=True,
                           input_field_placeholder='Виберіть пункт меню...')
