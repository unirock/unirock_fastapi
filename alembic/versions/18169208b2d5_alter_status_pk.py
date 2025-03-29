"""alter status pk

Revision ID: 18169208b2d5
Revises: e7cabaee4297
Create Date: 2025-03-28 13:23:58.126849

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '18169208b2d5'
down_revision: Union[str, None] = 'e7cabaee4297'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TABLE amo_statuses DROP CONSTRAINT amo_statuses_pkey CASCADE")
    op.create_primary_key("amo_statuses_pkey", "amo_statuses", ["id", "pipeline_id"])
    op.create_foreign_key(
        "fk_amo_status_id",
        "amo_leads",
        "amo_statuses",
        ["status_id", "pipeline_id"],
        ["id", "pipeline_id"]
    )


def downgrade() -> None:
    op.execute("ALTER TABLE amo_statuses DROP CONSTRAINT amo_statuses_pkey CASCADE")
    op.create_primary_key("amo_statuses_pkey", "amo_statuses", ["id"])
    op.create_foreign_key(
        "fk_amo_status_id",
        "amo_leads",
        "amo_statuses",
        ["status_id"],
        ["id"]
    )
