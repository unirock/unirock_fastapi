from enum import IntEnum

from core.entity import Base
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .lead import Lead


class StatusType(IntEnum):
    REGULAR = 0
    UNSORTED = 1


class Status(Base):
    __tablename__ = 'amo_statuses'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    sort_key: Mapped[int]
    is_editable: Mapped[bool]
    pipeline_id: Mapped[int] = mapped_column(ForeignKey('amo_pipelines.id'))
    color: Mapped[str]
    type: Mapped[StatusType] = mapped_column(Integer())
    account_id: Mapped[int]

    leads: Mapped[list[Lead]] = relationship()
