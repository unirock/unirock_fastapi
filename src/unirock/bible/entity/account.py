from datetime import datetime

from core.entity import Base
from sqlalchemy import TIMESTAMP, UUID, func
from sqlalchemy.orm import Mapped, mapped_column


class Account(Base):
    __tablename__ = 'accounts'

    id: Mapped[UUID] = mapped_column(UUID(), primary_key=True, server_default="gen_random_uuid()")
    name: Mapped[str] = mapped_column(nullable=False)

    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    created_by: Mapped[UUID] = mapped_column(nullable=False)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), onupdate=func.now(), nullable=True)
    updated_by: Mapped[UUID] = mapped_column(nullable=True)
    deleted_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
    deleted_by: Mapped[UUID] = mapped_column(nullable=True)
