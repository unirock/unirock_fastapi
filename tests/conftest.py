from pathlib import Path

import pytest_asyncio
from fastapi.testclient import TestClient
from dotenv import load_dotenv
file_path = Path(__file__).parent
load_dotenv(file_path.parent / ".env")
from asgi import app

@pytest_asyncio.fixture(scope="module", loop_scope="module")
def client():
    with TestClient(app) as client:
        yield client