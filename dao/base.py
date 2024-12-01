from sqlalchemy import select, insert
from database import SessionLocal


class BaseDAO:
    model = None

    @classmethod
    def find_one_or_none(cls, **filters):
        """
       Ищет одну запись в таблице, соответствующую фильтрам. Возвращает None, если запись не найдена.
       """
        with SessionLocal() as session:
            query = select(cls.model).filter_by(**filters)
            result = session.execute(query).scalar_one_or_none()
            return result

    @classmethod
    def filter_by(cls, **filters) -> list:
        """Возвращает записи из таблицы по переданному фильтру."""
        with SessionLocal() as session:
            query = select(cls.model).filter_by(**filters)
            result = session.execute(query)
            return result.scalars().all()

    @classmethod
    def add(cls, **data) -> None:
        """Добавляет новую запись в таблицу."""
        with SessionLocal() as session:
            query = insert(cls.model).values(**data)
            session.execute(query)
            session.commit()
