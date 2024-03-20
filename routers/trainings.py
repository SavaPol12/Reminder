from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from database.crud import get_user_words
from dependencies import db


from markups import start_markup
# from utils import view_result

router = Router()


class Training(StatesGroup):
    answer = State()


@router.message(Command("train"))
async def train(message: Message, state: FSMContext):
    await state.set_state(Training.answer)
    await state.update_data(words=get_user_words(db, message.from_user.id))
    await message.reply(
        "Тренировка началась!",
        reply_markup=start_markup(),
    )


async def print_word(message: Message, state: FSMContext):
    await message.answer()
