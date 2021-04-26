from gql_alchemy.database import db_session
from gql_alchemy.models.user import User


def test_all_user_query(client):
    add_users()
    response = client.post(
        "/graphql",
        json=get_all_users_payload(),
    )

    expected = {
        'data': {
            'allUsers': {
                'edges': [
                    {'node': {'familyName': 'Miller', 'givenName': 'Peter'}},
                    {'node': {'familyName': 'Milton', 'givenName': 'Anna'}}
                ]
            }
        }
    }
    assert response.status_code == 200
    assert expected == response.json()


def test_get_user_by_pk_query(client):
    add_users()
    response = client.post(
        "/graphql",
        json=get_user_by_pk_payload(),
    )

    expected = {
        'data': {
            'userById': {
                'edges': [
                    {'node': {'familyName': 'Miller', 'givenName': 'Peter'}}
                ]
            }
        }
    }
    assert response.status_code == 200
    assert expected == response.json()


def add_users():
    user1 = User(given_name="Peter", family_name="Miller")
    user2 = User(given_name="Anna", family_name="Milton")
    db_session.add(user1)
    db_session.add(user2)
    db_session.commit()


def get_all_users_payload():
    query = """
        query {
            allUsers {
                edges {
                    node {
                        givenName
                        familyName
                    }
                }
            }
        }
    """
    return {"query": query}


def get_user_by_pk_payload():
    query = """
        query {
            userById(pk: "1") {
                edges {
                    node {
                        givenName
                        familyName
                    }
                }
            }
        }
    """
    return {"query": query}
