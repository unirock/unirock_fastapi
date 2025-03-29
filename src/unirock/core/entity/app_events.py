from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from ._base import Base


class Audit(Base):
    __tablename__ = 'app_events'

    id: Mapped[UUID] = mapped_column(UUID(), primary_key=True, server_default="gen_random_uuid()")

    app: Mapped[str]
