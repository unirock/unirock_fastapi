import datetime
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP

from core.entity import Base
from sqlalchemy.orm import Mapped, mapped_column


class OfferConfigurationVersion(Base):
    __tablename__ = 'price_offer_configuration_versions'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    note: Mapped[str]
    

    project_id: Mapped[UUID] = mapped_column(ForeignKey('price_offer_projects.id'))
    configuration_id: Mapped[UUID] = mapped_column(ForeignKey('price_offer_configurations.id'))

    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True), auto_now_add=True)
    created_by: Mapped[UUID]

    updated_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True))
    updated_by: Mapped[UUID]

    is_archived: Mapped[bool] = mapped_column(default=False)
    archived_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP(timezone=True))
    archived_by: Mapped[UUID]

