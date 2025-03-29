"""create_amo_tables

Revision ID: e7cabaee4297
Revises: 
Create Date: 2025-03-26 16:44:01.282478

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'e7cabaee4297'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "amo_pipelines",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("sort_key", sa.Integer, nullable=False),
        sa.Column("is_main", sa.Boolean, nullable=False),
        sa.Column("is_unsorted_on", sa.Boolean, nullable=False),
        sa.Column("is_archive", sa.Boolean, nullable=False),
        sa.Column("account_id", sa.Integer, nullable=False),
    )
    op.create_table(
        "amo_statuses",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("sort_key", sa.Integer, nullable=False),
        sa.Column("is_editable", sa.Boolean, nullable=False),
        sa.Column("pipeline_id", sa.Integer, sa.ForeignKey('amo_pipelines.id', name='fk_amo_pipelines_id'),
                  nullable=False),
        sa.Column("color", sa.String, nullable=False),
        sa.Column("type", sa.Integer, nullable=False),
        sa.Column("account_id", sa.Integer, nullable=False),
    )
    op.create_index("ik_status_pipeline_id", "amo_statuses", ["pipeline_id"], unique=False)
    op.create_table(
        "amo_leads",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("price", sa.DECIMAL(5, 20, asdecimal=True)),
        sa.Column("responsible_user_id", sa.Integer),
        sa.Column("status_id", sa.Integer, sa.ForeignKey('amo_statuses.id', name='fk_amo_status_id'),
                  nullable=False),
        sa.Column("pipeline_id", sa.Integer, sa.ForeignKey('amo_pipelines.id', name='fk_amo_pipelines_id'),
                  nullable=False),
        sa.Column("group_id", sa.Integer),
        sa.Column("loss_reason_id", sa.Integer),
        sa.Column("source_id", sa.Integer),
        sa.Column("created_by", sa.Integer, nullable=False),
        sa.Column("updated_by", sa.Integer),
        sa.Column("closed_at", sa.TIMESTAMP(timezone=True)),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("updated_at", sa.TIMESTAMP(timezone=True)),
        sa.Column("is_deleted", sa.Boolean, nullable=False),
        sa.Column("account_id", sa.Integer, nullable=False),

        sa.Column("order_code", sa.String),
        sa.Column("primary_lead_id", sa.Integer),
    )
    op.create_index("ik_lead_pipeline_id", "amo_leads", ["pipeline_id"], unique=False)
    op.create_index("ik_lead_status_id", "amo_leads", ["status_id"], unique=False)
    op.create_index("ik_lead_order_code", "amo_leads", [sa.text("lower(order_code)")], unique=False)
    op.create_index("ik_lead_primary_lead_id", "amo_leads", ["primary_lead_id"], unique=False)
    op.create_index("ik_lead_name", "amo_leads", [sa.text("lower(name)")], unique=False)




def downgrade() -> None:
    op.drop_table("amo_statuses")
    op.drop_table("amo_pipelines")
    op.drop_table("amo_leads")
