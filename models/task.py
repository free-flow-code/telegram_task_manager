from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum


class TaskStatus(enum.Enum):
    done = "Выполнена"
    not_done = "Не выполнена"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    is_done = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.not_done)

    user = relationship("User", back_populates="tasks")

    def __repr__(self):
        return f"<Task(id={self.id}, description={self.description[:20]}, is_done={self.is_done})>"
