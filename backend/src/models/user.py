from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from uuid import UUID, uuid4
from datetime import datetime
import enum

if TYPE_CHECKING:
    from .task import Task


class UserRole(str, enum.Enum):
    USER = "user"
    ADMIN = "admin"


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(unique=True, nullable=False, max_length=255)
    password_hash: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)
    role: UserRole = Field(default=UserRole.USER)

    # Relationship to tasks
    tasks: list["Task"] = Relationship(back_populates="user")

    def __str__(self):
        return f"User(id={self.id}, email={self.email})"

    def __repr__(self):
        return self.__str__()