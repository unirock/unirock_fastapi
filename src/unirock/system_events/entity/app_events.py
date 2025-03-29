from datetime import datetime
from typing import Any

from core.entity import Base
from sqlalchemy import JSON, TIMESTAMP, UUID, func
from sqlalchemy.orm import Mapped, mapped_column


class SystemEvent(Base):
    __tablename__ = 'system_events'

    id: Mapped[UUID] = mapped_column(UUID(), primary_key=True, server_default="gen_random_uuid()")

    app: Mapped[str] = mapped_column(UUID(), nullable=False)
    type: Mapped[str]
    error: Mapped[str]
    timestamp: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    details_json: Mapped[dict[str, Any]] = mapped_column(JSON(), nullable=False)

    user_id: ...
    user_token_iss: ...
    ip_address: ...
