import phonenumbers
from typing import Optional
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states import RegistrationStates


def validate_phonenumber(phonenumber: str) -> Optional[int]:
    """Проверяет корректность введенного номера телефона.
    Принимает номер телефона в международном формате.
    """
    try:
        parsed_phone = phonenumbers.parse(phonenumber, None)
        is_valid_number = phonenumbers.is_valid_number(parsed_phone)

        if not is_valid_number:
            raise phonenumbers.phonenumberutil.NumberParseException(0, "Invalid phone number")

        return int(''.join(filter(str.isdigit, phonenumber)))
    except phonenumbers.phonenumberutil.NumberParseException:
        return


async def redirect_to_registration(message: Message, state: FSMContext) -> None:
    """Перенаправляет пользователя на регистрацию."""
    await message.answer(
        "Вы не зарегистрированы! Давайте исправим это."
    )
    await message.answer("Введите ваше имя для регистрации:")
    await state.set_state(RegistrationStates.enter_name)
    return
