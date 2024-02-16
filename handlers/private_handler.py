from aiogram.filters import Command
from aiogram import types, Router
from custom_filters.chat_type_filter import ChatTypeFilter


private_router = Router()
private_router.message.filter(ChatTypeFilter(['private']))

@private_router.message(Command('start'))
async def hello_cmd(message: types.Message):
    await message.answer('Hello world!')


private_router