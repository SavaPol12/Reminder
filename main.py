import asyncio
import logging
from os import getenv
from typing import NoReturn

from aiogram import Bot, Dispatcher
from database.config import Base, engine

# from database.crud import get_user, get_users
from routers import commands, dictionaries, trainings


async def main() -> NoReturn:
    logging.basicConfig(level=logging.INFO)

    Base.metadata.create_all(bind=engine)
    TOKEN: str = getenv("TG_TOKEN") or ""

    TOKEN = "6485653271:AAHnytqZ3XD1LtBroYskpUdUg9CN4NvURJc"
    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_router(commands.router)
    dp.include_router(dictionaries.router)
    dp.include_router(trainings.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
