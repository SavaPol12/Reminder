from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_markup():
    kb = ReplyKeyboardBuilder()
    kb.button(text='/start')
    kb.button(text='/create')
    kb.button(text='/view')
    kb.button(text='/help')

    return kb.as_markup()
