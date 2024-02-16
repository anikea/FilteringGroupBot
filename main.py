import os
import asyncio

from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv, find_dotenv
from aiogram.filters import Command

from handlers.private_handler import private_router
from handlers.group_handler import group_handler

load_dotenv(find_dotenv())


bot = Bot(token=os.getenv('TOKEN'), parse_mode='HTML')
dp = Dispatcher()

dp.include_router(private_router)
dp.include_router(group_handler)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())