from gql_alchemy.models.user import User


def test_add_user_mutation(client):
    response = client.post(
        "/graphql",
        json=get_mutation_query(),
    )

    expected = {
        'data': {
            'addUser': {
                'user': {'givenName': 'Elisabeth', 'familyName': 'Müller'},
                'ok': True
            }
        }
    }

    assert response.status_code == 200
    assert expected == response.json()
    assert 1 == len(User.query.all())
    assert "Elisabeth" == User.query.first().given_name
    assert "Müller" == User.query.first().family_name


def get_mutation_query():
    query = """
        mutation {
          addUser(familyName: "Müller", givenName: "Elisabeth") {
            user {
              givenName
              familyName
            }
            ok
          }
        }
    """
    return {"query": query}
