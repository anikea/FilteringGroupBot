from aiogram import types, Router, F
from aiogram.filters import Command
from custom_filters.chat_type_filter import ChatTypeFilter


group_handler = Router()
group_handler.message.filter(ChatTypeFilter(['group']))


@group_handler.message(Command('hello'))
async def hello_cmd(message: types.Message):
    await message.answer(f'Hello {message.from_user.first_name}!')
