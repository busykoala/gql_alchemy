from graphene_sqlalchemy import SQLAlchemyConnectionField

from gql_alchemy.models.user import User


class UserByIdConn(SQLAlchemyConnectionField):
    @classmethod
    def get_query(cls, model, info, **args):
        cls.query = User.query.filter(User.pk == args["pk"])
        return cls.query
