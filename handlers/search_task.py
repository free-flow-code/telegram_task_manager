import textwrap
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states import SearchTaskState
from models.models_dao import UserDAO, TaskDAO
from utils import redirect_to_registration

router = Router()


@router.message(Command("search"))
async def search_task(message: Message, state: FSMContext):
    user = UserDAO.find_one_or_none(telegram_id=message.from_user.id)
    if not user:
        await redirect_to_registration(message, state)
        return

    await state.update_data(user_id=user.id)
    await message.answer("Введите слово или фразу для поиска задачи:")
    await state.set_state(SearchTaskState.enter_keyword)


@router.message(SearchTaskState.enter_keyword)
async def enter_keyword(message: Message, state: FSMContext):
    data = await state.get_data()
    tasks = TaskDAO.search_task_by_keyword(data["user_id"], message.text)

    if not tasks:
        await message.answer("Нет задач, подходящих критериям поиска.")
        return

    reply_message = ""
    for task in tasks:
        reply_message += textwrap.dedent(f"""\
            *Задача №{task.id}*
            *Название:* {task.title.strip()}
            *Описание:*
            {task.description.strip()}
            *Статус:* {'Выполнена' if task.is_done == "done" else 'Не выполнена'}\n
            """)
    await message.answer(
        reply_message,
        parse_mode="MarkdownV2"
    )
    await state.clear()
