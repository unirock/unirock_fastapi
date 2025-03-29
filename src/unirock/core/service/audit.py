from uuid import UUID

from ..entity.audit import Audit


async def create_audit_record(before: dict, after: dict, user_id: UUID) -> Audit:
    entry = Audit(

    )