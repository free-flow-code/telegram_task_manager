from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from states import TaskStates, RegistrationStates
from models.models_dao import UserDAO, TaskDAO

router = Router()


@router.message(Command("add"))
async def add_task_start(message: Message, state: FSMContext):
    # Если пользователь не зарегистрирован, предлагаем зарегистрироваться
    user = UserDAO.find_one_or_none(telegram_id=message.from_user.id)
    if not user:
        await message.answer(
            "Вы не зарегистрированы! Давайте исправим это."
        )
        await message.answer("Введите ваше имя для регистрации:")
        await state.set_state(RegistrationStates.enter_name)
        return

    await state.update_data(user_id=user.id)
    await message.answer("Введите название задачи:")
    await state.set_state(TaskStates.enter_task_name)


@router.message(TaskStates.enter_task_name)
async def enter_task_name(message: Message, state: FSMContext):
    if TaskDAO.find_one_or_none(title=message.text):
        await message.answer("Задача с таким названием уже существует. Выберите другое:")
        return

    await state.update_data(name=message.text)
    await message.answer("Добавьте описание задачи:")
    await state.set_state(TaskStates.enter_description)


@router.message(TaskStates.enter_description)
async def save_task(message: Message, state: FSMContext):
    data = await state.get_data()

    TaskDAO.add(user_id=data["user_id"], title=data["name"], description=message.text)

    await message.answer("Задача добавлена!")
    await state.clear()
