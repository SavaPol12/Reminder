from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from database.crud import get_user_words
from dependencies import db

from markups import start_markup
from utils import readable_format


router = Router()


class Training(StatesGroup):
    answers = State()
    summary = State()


@router.message(F.text == "Тренировка")
async def train(message: Message, state: FSMContext):
    user_words = list(get_user_words(db, message.from_user.id))[::-1]
    if not len(user_words):
        return await message.answer(
            "У тебя нет слов",
            reply_markup=start_markup(),
        )
    await message.answer(
        "Тренировка началась!",
    )
    await message.answer(
        f"Введи перевод этого слова: {user_words.pop()}",
    )
    await state.update_data(
        words=user_words,
        answers=[],
    )

    await state.set_state(Training.answers)


@router.message(Training.answers)
async def print_word(message: Message, state: FSMContext):
    data = await state.get_data()
    data["answers"].append(message.text)

    cur_word = data["words"].pop()

    if len(data["words"]) == 0:
        await state.set_state(Training.summary)
        return await message.answer(f"Последнее слово: {cur_word}")

    await message.answer(f"Введи перевод этого слова: {cur_word}")


@router.message(Training.summary)
async def training_summary(message: Message, state: FSMContext):
    data = await state.get_data()
    data["answers"].append(message.text)

    result_text = "\n".join(data["answers"])

    await message.answer(f"Твои ответы:\n{result_text}")

    u_words = get_user_words(db, message.from_user.id)
    await message.answer(
        f"Словарь:\n{readable_format(u_words)}",
    )

    await state.clear()
