import httpx

class CBRClient(httpx.AsyncClient):

    def __init__(self, *args, **kwargs):
        kwargs["base_url"] = "https://www.cbr.ru"
        super().__init__(*args, **kwargs)