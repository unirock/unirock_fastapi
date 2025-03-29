from core.entity import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .lead import Lead
from .status import Status


class Pipeline(Base):
    __tablename__ = 'amo_pipelines'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    sort_key: Mapped[int]
    is_main: Mapped[bool]
    is_unsorted_on: Mapped[bool]
    is_archive: Mapped[bool]
    account_id: Mapped[int]
    statuses: Mapped[list[Status]] = relationship(lazy='joined', order_by="Status.sort_key")
    leads: Mapped[list[Lead]] = relationship()
