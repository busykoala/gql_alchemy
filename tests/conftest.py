from fastapi.testclient import TestClient
import pytest

from gql_alchemy.app import app


@pytest.fixture
def client():
    return TestClient(app)
