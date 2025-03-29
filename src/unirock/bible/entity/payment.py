from datetime import datetime
from decimal import Decimal

from core.entity._base import Base
from sqlalchemy import DECIMAL, TIMESTAMP, UUID, BigInteger, func
from sqlalchemy.orm import Mapped, mapped_column


class Payment(Base):
    __tablename__ = 'payments'

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, server_default="gen_random_uuid()")

    amo_lead_id: Mapped[int] = mapped_column(BigInteger, nullable=True)

    value: Mapped[Decimal] = mapped_column(DECIMAL(15, 5))
    account_id: ...
    counterparty_id: ...
    direction: ...

    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    created_by: Mapped[UUID] = mapped_column(nullable=False)
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), onupdate=func.now(), nullable=True)
    updated_by: Mapped[UUID] = mapped_column(nullable=True)
    deleted_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True)
    deleted_by: Mapped[UUID] = mapped_column(nullable=True)


class PaymentBatch(Base):
    ...

class PaymentBatchLink(Base):
    ...