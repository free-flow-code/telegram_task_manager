from typing import Optional
import phonenumbers


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
