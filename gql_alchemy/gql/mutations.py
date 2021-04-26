from graphene import ObjectType

from gql_alchemy.gql.mutation_types import AddUser


class GqlMutation(ObjectType):
    add_user = AddUser().Field()
