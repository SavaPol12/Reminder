import asyncio
from os import getenv
from typing import NoReturn

from aiogram import Bot, Dispatcher
from database.config import Base, engine

# from database.crud import get_user, get_users
from routers import commands, dictionaries


async def main() -> NoReturn:
    Base.metadata.create_all(bind=engine)
    TOKEN: str = getenv("TG_TOKEN") or ""

    TOKEN = "6485653271:AAHnytqZ3XD1LtBroYskpUdUg9CN4NvURJc"
    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_router(commands.router)
    dp.include_router(dictionaries.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    #    print(get_users(db))
    #    print(get_user(db, ))
    asyncio.run(main())
