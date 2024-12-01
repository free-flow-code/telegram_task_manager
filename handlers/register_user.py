from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from states import RegistrationStates

from models.models_dao import UserDAO
from utils import validate_phonenumber

router = Router()


@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    if UserDAO.find_one_or_none(telegram_id=message.from_user.id):
        await message.answer("С возвращением!")
        return

    await message.answer("Привет! Давайте зарегистрируемся. Введите ваше имя:")
    await state.set_state(RegistrationStates.enter_name)


@router.message(RegistrationStates.enter_name)
async def enter_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Отлично! Теперь введите ваш номер телефона в формате +79998887766:")
    await state.set_state(RegistrationStates.enter_phone)


@router.message(RegistrationStates.enter_phone)
async def enter_phone(message: Message, state: FSMContext):
    validate_phone = validate_phonenumber(message.text)

    if not validate_phone:
        await message.answer("Некорректный номер телефона. Введите ваш номер телефона в формате +79998887766:")
        return

    data = await state.get_data()
    name = data["name"]

    UserDAO.add(telegram_id=message.from_user.id, name=name, phone=validate_phone)

    await message.answer("Регистрация завершена!")
    await state.clear()
