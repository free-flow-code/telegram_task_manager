from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from models.task import TaskStatus
from states import DeleteTaskState
from models.models_dao import UserDAO, TaskDAO
from utils import redirect_to_registration
from keyboards.user_keyboards import delete_task_keyboard

router = Router()


@router.message(Command("delete"))
async def delete_task(message: Message, state: FSMContext):
    user = UserDAO.find_one_or_none(telegram_id=message.from_user.id)
    if not user:
        await redirect_to_registration(message, state)
        return

    await state.update_data(user_id=user.id)
    await message.answer(
        "Вы действительно хотите удалить все выполненные задачи?",
        reply_markup=delete_task_keyboard()
    )
    await state.set_state(DeleteTaskState.delete_confirmation)


@router.callback_query(DeleteTaskState.delete_confirmation)
async def delete_confirmation(callback: CallbackQuery, state: FSMContext):
    is_confirm = callback.data
    if is_confirm == "yes":
        data = await state.get_data()
        tasks = TaskDAO.filter_by(user_id=data["user_id"], is_done=TaskStatus.done)

        if not tasks:
            await callback.message.answer("Нет задач для удаления.")
            return

        for task in tasks:
            TaskDAO.delete(task.id)

        await callback.message.answer("Выполненные задачи успешно удалены!")
    await state.clear()
