from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from database.crud import get_user, update_users_words

from utils import normalize_word
from dependencies import db

router = Router()

words = {}


class NewWord(StatesGroup):
    word = State()
    translation = State()


@router.message(F.text == "Добавить слово")
async def start_dictionary(message: Message, state: FSMContext):
    await state.set_state(NewWord.word)
    await message.answer(
        "Введите новое слово на знакомом языке",
    )


@router.message(NewWord.word)
async def add_word(message: Message, state: FSMContext):
    await state.update_data(word=message.text)
    await message.answer("Введите перевод этого слова")
    await state.set_state(NewWord.translation)


@router.message(NewWord.translation)
async def add_transtation(message: Message, state: FSMContext):
    await state.update_data(translation=message.text)
    await message.answer("Слово и перевод успешно сохраненны!")
    data = await state.get_data()
    await state.clear()
    user = get_user(db, message.from_user.id)
    lol = update_users_words(db, user, normalize_word(data))
    print(lol)
