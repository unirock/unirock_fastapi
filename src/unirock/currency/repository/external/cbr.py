import datetime

from httpx import AsyncClient
from ...client.cbr import CBRClient


class CBRRepository:

    def __init__(self, client: CBRClient):
        self.client = client

    async def get_currency_quotation_list_for_today(self):
        today = datetime.date.today()
        return await self.get_currency_quotation_list_for_date(today)

    async def get_currency_quotation_list_for_date(self, date: datetime.date):
        url = "/scripts/XML_daily.asp"
        f_date = date.strftime('%d/%m/%Y')
        response = await self.client.get(url, params={
            "date_req": f_date
        })
        response.raise_for_status()
        return response.content

    async def get_currency_dict(self):
        url = "/scripts/XML_valFull.asp"
        response = await self.client.get(url, params={"d": 0})
