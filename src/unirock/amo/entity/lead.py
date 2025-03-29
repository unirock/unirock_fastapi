import datetime
from decimal import Decimal

from core.entity import Base
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column


class Lead(Base):
    __tablename__ = 'amo_leads'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    price: Mapped[Decimal]
    responsible_user_id: Mapped[int]
    status_id: Mapped[int] = mapped_column(ForeignKey('amo_statuses.id'))
    pipeline_id: Mapped[int] = mapped_column(ForeignKey('amo_pipelines.id'))
    group_id: Mapped[int]
    loss_reason_id: Mapped[int]
    source_id: Mapped[int]
    created_by: Mapped[int]
    updated_by: Mapped[int]
    closed_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True))
    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True))
    updated_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True))
    is_deleted: Mapped[bool]
    account_id: Mapped[int]

    order_code: Mapped[str]
    primary_lead_id: Mapped[int]
