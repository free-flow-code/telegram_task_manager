from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from database import Base
import pytz

from config import settings


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    registration_date = Column(
        Date,
        nullable=False,
        default=datetime.now(tz=pytz.timezone(settings.SERVER_TZ)).timestamp()
    )

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, telegram_id={self.telegram_id})>"
