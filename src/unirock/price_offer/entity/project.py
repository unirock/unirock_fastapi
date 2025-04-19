import datetime
from decimal import Decimal
from uuid import UUID

from sqlalchemy.dialects.postgresql import TIMESTAMP
from core.entity import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .configuration import OfferConfiguration


class OfferProject(Base):
    __tablename__ = 'price_offer_projects'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str]

    configurations: Mapped[list[OfferConfiguration]] = relationship()

    related_lead_id: Mapped[int] = mapped_column(ForeignKey('amo_leads.id'))

    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True), auto_now_add=True)
    created_by: Mapped[UUID]

    updated_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True))
    updated_by: Mapped[UUID]

    is_archived: Mapped[bool] = mapped_column(default=False)
    archived_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True))
    archived_by: Mapped[UUID]
