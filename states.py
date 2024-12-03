from aiogram.fsm.state import State, StatesGroup


class RegistrationStates(StatesGroup):
    enter_name = State()
    enter_phone = State()


class AddTaskStates(StatesGroup):
    enter_task_name = State()
    enter_description = State()


class ManageTaskStates(StatesGroup):
    enter_task_number = State()
    choose_status = State()


class DeleteTaskState(StatesGroup):
    delete_confirmation = State()


class SearchTaskState(StatesGroup):
    enter_keyword = State()
