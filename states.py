from aiogram.fsm.state import State, StatesGroup


class RegistrationStates(StatesGroup):
    enter_name = State()
    enter_phone = State()


class TaskStates(StatesGroup):
    enter_task_name = State()
    enter_description = State()
