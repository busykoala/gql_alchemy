from graphene import Boolean
from graphene import Field
from graphene import Mutation
from graphene import String

from gql_alchemy.database import db_session
from gql_alchemy.gql.schemas import UserNode
from gql_alchemy.models.user import User
from gql_alchemy.gql.types import UserType


class AddUser(Mutation):
    class Arguments:
        given_name = String(required=True)
        family_name = String(required=True)

    ok = Boolean()
    user = Field(lambda: UserNode)

    def mutate(self, info, given_name, family_name):
        try:
            user_data = UserType(
                given_name=given_name,
                family_name=family_name)
            new_user = User(**user_data.dict())
            db_session.add(new_user)
            db_session.commit()
            ok = True
        except Exception:
            ok = False
            new_user = None

        return AddUser(user=new_user, ok=ok)
