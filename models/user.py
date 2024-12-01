from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
import pytz

from config import settings
from models.task import Task


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    registration_date = Column(
        Float,
        nullable=False,
        default=datetime.now(tz=pytz.timezone(settings.SERVER_TZ)).timestamp()
    )

    tasks = relationship("Task", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, telegram_id={self.telegram_id})>"
