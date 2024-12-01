from aiogram.utils.keyboard import InlineKeyboardBuilder


def change_task_status_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Выполнена", callback_data="done")
    keyboard.button(text="Не выполнена", callback_data="not_done")
    keyboard.adjust(2)
    return keyboard.as_markup()


def delete_task_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Да", callback_data="yes")
    keyboard.button(text="Нет", callback_data="no")
    keyboard.adjust(2)
    return keyboard.as_markup()
