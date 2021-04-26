import pytest
from fastapi.testclient import TestClient

from gql_alchemy.app import app
from gql_alchemy.database import db_session
from gql_alchemy.models.user import User


@pytest.fixture(scope="function")
def client():
    stupid_cleanup()
    return TestClient(app)


def stupid_cleanup():
    User.query.delete()
    db_session.commit()
