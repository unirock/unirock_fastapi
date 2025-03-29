from datetime import datetime

from core.entity._base import Base
from sqlalchemy import ARRAY, TIMESTAMP, UUID, VARCHAR, func
from sqlalchemy.orm import Mapped, mapped_column

from bible.enums import CounterpartyType


class Counterparty(Base):
    __tablename__ = 'counterparties'

    id: Mapped[UUID] = mapped_column(UUID(), primary_key=True, server_default="gen_random_uuid()")

    name: Mapped[str]

    type: Mapped[CounterpartyType]
    is_service: Mapped[bool] = mapped_column(server_default="false")

    tags: Mapped[list[str]] = mapped_column(ARRAY(VARCHAR()))

    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    created_by: Mapped[UUID] = mapped_column(nullable=False)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), onupdate=func.now(), nullable=True)
    updated_by: Mapped[UUID] = mapped_column(nullable=True)
    deleted_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
    deleted_by: Mapped[UUID] = mapped_column(nullable=True)
