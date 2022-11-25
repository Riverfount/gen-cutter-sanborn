import pytest
from starlette.testclient import TestClient

from api.main import api


@pytest.fixture
def client():
    return TestClient(app=api)
