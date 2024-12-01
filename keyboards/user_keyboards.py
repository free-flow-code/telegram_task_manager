from aiogram.utils.keyboard import InlineKeyboardBuilder


def change_task_status_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Выполнена", callback_data="done")
    keyboard.button(text="Не выполнена", callback_data="not_done")
    keyboard.adjust(2)
    return keyboard.as_markup()
