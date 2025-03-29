from amo import AmoClient

from ...repository.external.lead import AmoLeadRepository
from ...schema.external import ExternalLeadListPageResponseDto


class ExternalLeadService:

    def __init__(self, amo_client: AmoClient):
        self.repository = AmoLeadRepository(amo_client)

    async def get_leads_page(self, page: int, limit: int):
        leads_page = await self.repository.get_leads_page(page, limit)
        return leads_page
