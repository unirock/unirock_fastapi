from datetime import date

from shared.repository.database.connection import get_session

from ..service import SystemEventService


async def vacuum_events() -> None:
    vacuum_before: date = date.today()
    async with get_session() as session:
        service = SystemEventService(session)
        await service.vacuum_events(to_date=vacuum_before)

    return None
