from sqlalchemy import select, func
from dao.base import BaseDAO
from models.user import User
from models.task import Task
from database import SessionLocal
from models.task import TaskStatus


class UserDAO(BaseDAO):
    model = User


class TaskDAO(BaseDAO):
    model = Task

    @classmethod
    def search_task_by_keyword(cls, user_id: int, keyword: str, task_status: TaskStatus = TaskStatus.not_done):
        with SessionLocal() as session:
            query = select(cls.model).where(
                cls.model.user_id == user_id,
                func.lower(cls.model.title).like(f"%{keyword.lower()}%"),
                cls.model.is_done == task_status
            )
            result = session.execute(query)
            return result.scalars().all()
