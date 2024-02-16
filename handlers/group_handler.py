from aiogram import types, Router, F
from aiogram.filters import Command
from custom_filters.chat_type_filter import ChatTypeFilter
import re

group_handler = Router()
group_handler.message.filter(ChatTypeFilter(['group']))

# Регулярний вираз для фіксування всіх слів "Онлайн"
work_ukraine_pattern = re.compile(r'онлайн', re.IGNORECASE)
work_ukraine = '#РоботаУкраїна'

# Регулярний вираз для фіксування всіх слів "Україн" - тобто очної роботи
work_online_pattern = re.compile(r'україн', re.IGNORECASE)
work_online = "#РоботаОнлайн"

@group_handler.message(F.text.contains(work_ukraine))
@group_handler.edited_message()
async def hello_ukr_cmd(message: types.Message):
    # Перевірка, чи містить текст повідомлення заборонені слова
    if work_ukraine_pattern.search(message.text):
        try:
            await message.delete()
            await message.answer(f'{message.from_user.first_name}, слідкуйте за правилами чату.')
        except AttributeError:
            print('SomeText')
            
            
@group_handler.message(F.text.contains(work_online))
@group_handler.edited_message()
async def hello_ukr_cmd(message: types.Message):
    # Перевірка, чи містить текст повідомлення заборонені слова
    if work_online_pattern.search(message.text):
        try:
            await message.delete()
            await message.answer(f'{message.from_user.first_name}, слідкуйте за правилами чату.')
        except AttributeError:
            print('SomeText')
