"""fix_lead_price_precision_scale

Revision ID: b4ee858acc2b
Revises: 18169208b2d5
Create Date: 2025-03-28 16:44:50.354598

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'b4ee858acc2b'
down_revision: Union[str, None] = '18169208b2d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "amo_leads",
        "price",
        existing_type=sa.DECIMAL(5, 20, asdecimal=True),
        type_=sa.DECIMAL(20, 5, asdecimal=True),
    )


def downgrade() -> None:
    op.alter_column(
        "amo_leads",
        "price",
        existing_type=sa.DECIMAL(20, 5, asdecimal=True),
        type_=sa.DECIMAL(5, 20, asdecimal=True),
    )