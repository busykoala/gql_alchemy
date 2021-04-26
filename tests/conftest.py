from fastapi.testclient import TestClient
import pytest

from gql_alchemy.app import app
from gql_alchemy.models.user import User
from gql_alchemy.database import db_session


@pytest.fixture(scope="function")
def client():
    stupid_cleanup()
    return TestClient(app)


def stupid_cleanup():
    User.query.delete()
    db_session.commit()
