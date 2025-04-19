import datetime
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP, JSONB

from core.entity import Base
from sqlalchemy.orm import Mapped, mapped_column

from price_offer.entity.offer_version import OfferConfigurationVersion


class OfferConfiguration(Base):
    __tablename__ = 'price_offer_configurations'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str]
    configuration_data: Mapped[dict] = mapped_column(JSONB(none_as_null=True))
    versions: Mapped[list[OfferConfigurationVersion]]

    project_id: Mapped[UUID] = mapped_column(ForeignKey('price_offer_projects.id'))

    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True), auto_now_add=True)
    created_by: Mapped[UUID]

    updated_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True))
    updated_by: Mapped[UUID]

    is_archived: Mapped[bool] = mapped_column(default=False)
    archived_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True))
    archived_by: Mapped[UUID]
