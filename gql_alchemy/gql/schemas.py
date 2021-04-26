from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from gql_alchemy.models.user import User


class UserNode(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node,)
