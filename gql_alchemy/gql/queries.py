from graphene import Argument as GqlArgument
from graphene import ObjectType
from graphene import String as GqlString
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField

from gql_alchemy.gql.connections import UserByIdConn
from gql_alchemy.gql.schemas import UserNode


class GqlQuery(ObjectType):
    node = relay.Node.Field()

    # Open data from model
    all_users = SQLAlchemyConnectionField(UserNode.connection)

    # Build own query by arguments
    user_by_id = UserByIdConn(
        UserNode.connection,
        args={"pk": GqlArgument(GqlString), },
        required=True,
    )
