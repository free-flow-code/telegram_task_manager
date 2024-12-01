from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from models.task import TaskStatus
from states import ManageTaskStates
from models.models_dao import UserDAO, TaskDAO
from utils import redirect_to_registration
from keyboards.user_keyboards import change_task_status_keyboard

router = Router()


@router.message(Command("manage"))
async def change_task_status(message: Message, state: FSMContext):
    user = UserDAO.find_one_or_none(telegram_id=message.from_user.id)
    if not user:
        await redirect_to_registration(message, state)
        return

    await state.update_data(user_id=user.id)
    await message.answer("Чтобы изменить статус задачи, введите ее номер:")
    await state.set_state(ManageTaskStates.enter_task_number)


@router.message(ManageTaskStates.enter_task_number)
async def enter_task_number(message: Message, state: FSMContext):
    try:
        task_number = int(message.text)
    except ValueError:
        await message.answer("Номер задачи должен быть числом! Попробуйте еще раз:")
        return

    data = await state.get_data()
    task = TaskDAO.filter_by(id=task_number, user_id=data["user_id"])

    if not task:
        await message.answer("Такой задачи не существует. Попробуйте еще раз:")
        return

    await state.update_data(task_id=task_number)
    await message.answer(
        "Выберите новый статус задачи:",
        reply_markup=change_task_status_keyboard()
    )
    await state.set_state(ManageTaskStates.choose_status)


@router.callback_query(ManageTaskStates.choose_status)
async def change_task_status_callback(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    new_status = callback.data
    if new_status == "done":
        is_done = TaskStatus.done
    elif new_status == "not_done":
        is_done = TaskStatus.not_done
    else:
        await callback.message.answer("Некорректный выбор. Попробуйте снова.")
        return

    TaskDAO.edit(data["task_id"], is_done=is_done)

    await callback.message.answer(
        f"Статус задачи №{data['task_id']} успешно обновлен на {'Выполнена' if is_done else 'Не выполнена'}!"
    )
    await state.clear()
