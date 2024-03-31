from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_markup():
    kb = ReplyKeyboardBuilder()
    kb.button(text="Добавить слово")
    kb.button(text="Словарь")
    kb.button(text="Тренировка")
    kb.button(text="На главную")
    kb.button(text="Справка")

    return kb.adjust(2, 1, 2).as_markup()


def cancel_markup():
    kb = ReplyKeyboardBuilder()
    kb.button(text="Выход")

    return kb.as_markup()
