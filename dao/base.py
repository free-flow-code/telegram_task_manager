from typing import Optional
from sqlalchemy import select, insert
from database import SessionLocal
from models.user import User


class BaseDAO:
    model = None

    @classmethod
    def find_one_or_none(cls, **filters) -> Optional[User]:
        """
       Ищет одну запись в таблице, соответствующую фильтрам. Возвращает None, если запись не найдена.
       """
        with SessionLocal() as session:
            query = select(cls.model).filter_by(**filters)
            result = session.execute(query).scalar_one_or_none()
            return result

    @classmethod
    def add(cls, **data) -> None:
        """Добавляет новую запись в таблицу."""
        with SessionLocal() as session:
            query = insert(cls.model).values(**data)
            result = session.execute(query)
            session.commit()
