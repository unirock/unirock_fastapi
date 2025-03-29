import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class AmoLeadResponseDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    price: Decimal
    responsible_user_id: int
    status_id: int
    pipeline_id: int
    group_id: int
    loss_reason_id: int
    source_id: int
    created_by: int
    updated_by: int
    closed_at: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    is_deleted: bool
    account_id: int
    order_code: str
    primary_lead_id: int
