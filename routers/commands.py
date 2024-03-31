from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from database.crud import create_user


from markups import start_markup
from dependencies import db

router = Router()


@router.message(F.text == "На главную")
async def start(message: Message):
    create_user(db, message.from_user.id)
    await message.reply(
        "Привет! Данный бот находится в разработке:D Загляни позже...",
        reply_markup=start_markup(),
    )


@router.message(F.text == "Справка")
async def help(message: Message):
    await message.reply("Обратитесь в поддержку:D", reply_markup=start_markup())


@router.message(F.text == "Выход")
async def cancel(message: Message, state: FSMContext):
    await message.reply("Понял тебя", reply_markup=start_markup())
    await state.clear()
