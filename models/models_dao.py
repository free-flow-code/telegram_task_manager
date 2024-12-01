from dao.base import BaseDAO
from models.user import User
from models.task import Task


class UserDAO(BaseDAO):
    model = User


class TaskDAO(BaseDAO):
    model = Task
