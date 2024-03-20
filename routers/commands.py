from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from database.crud import create_user, get_user, get_user_words


from markups import start_markup
from dependencies import db
from utils import readable_format
# from utils import view_result

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    create_user(db, message.from_user.id)
    await message.reply(
        "Привет! Данный бот находится в разработке:D Загляни позже...",
        reply_markup=start_markup(),
    )


@router.message(Command("help"))
async def help(message: Message):
    await message.reply("Обратитесь в поддержку:D", reply_markup=start_markup())


@router.message(Command("create"))
async def create(message: Message):
    await message.reply(
        "Составьте свой сборник слов. Данная функция скоро станет доступна",
        reply_markup=start_markup(),
    )


@router.message(Command("view"))
async def view(message: Message):
    u_words = get_user_words(db, message.from_user.id)
    await message.reply(
        readable_format(u_words),
        reply_markup=start_markup(),
    )
