import textwrap
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from models.models_dao import UserDAO, TaskDAO
from utils import redirect_to_registration

router = Router()


@router.message(Command("tasks"))
async def view_task_list(message: Message, state: FSMContext):
    user = UserDAO.find_one_or_none(telegram_id=message.from_user.id)
    if not user:
        await redirect_to_registration(message, state)
        return

    tasks = TaskDAO.filter_by(user_id=user.id)
    reply_message = ""
    for task in tasks:
        reply_message += textwrap.dedent(f"""\
        *Задача №{task.id}*
        *Название:* {task.title.strip()}
        *Описание:*
        {task.description.strip()}
        *Статус:* {'Выполнена' if task.is_done else 'Не выполнена'}\n
        """)
    await message.answer(
        reply_message if reply_message else "У вас пока нет задач!",
        parse_mode="MarkdownV2"
    )
