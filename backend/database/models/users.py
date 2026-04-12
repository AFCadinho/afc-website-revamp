import sqlalchemy as sa

from sqlalchemy.orm import Mapped, mapped_column
from database.base import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(64), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(sa.String(255), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(sa.String(255), nullable=False)

    is_email_confirmed: Mapped[bool] = mapped_column(sa.Boolean, server_default=sa.false(), nullable=False)
    is_admin: Mapped[bool] = mapped_column(sa.Boolean, server_default=sa.false(), nullable=False)
    is_banned: Mapped[bool] = mapped_column(sa.Boolean, server_default=sa.false(), nullable=False)

    created_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False)

