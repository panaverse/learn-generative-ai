from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from sqlalchemy import String, Boolean, UUID, DateTime, Enum

import datetime
import uuid
import enum

class RoleEnum(enum.Enum):
    """
    Enumeration class representing different roles.
    """
    admin = 'admin'
    user = 'user'


class Base(DeclarativeBase):
    pass


class USER(Base):
    """
    Represents a User in the database.
    """
    __tablename__ = "users_table"

    id: Mapped[UUID] = mapped_column(
        UUID, primary_key=True, index=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String, unique=True, index=True)
    username: Mapped[str] = mapped_column(String, unique=True, index=True)
    full_name: Mapped[str] = mapped_column(String)
    hashed_password: Mapped[str] = mapped_column(String, index=True)
    email_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    role: Mapped[RoleEnum] = mapped_column(Enum(RoleEnum), default=RoleEnum.user)
    disabled: Mapped[bool] = mapped_column(Boolean, default=False)

    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc))
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=lambda: datetime.datetime.now(datetime.timezone.utc), onupdate=lambda: datetime.datetime.now(datetime.timezone.utc))

