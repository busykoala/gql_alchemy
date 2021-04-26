from alembic import command
from fastapi import FastAPI
from graphene import Schema
from starlette.graphql import GraphQLApp

from gql_alchemy.config import get_conf
from gql_alchemy.database import Base
from gql_alchemy.database import engine
from gql_alchemy.gql.mutations import GqlMutation
from gql_alchemy.gql.queries import GqlQuery

# setup database
app_tables = [
    "tbl_user",
]
tables = [
    tbl
    for tbl_name, tbl in Base.metadata.tables.items()
    if tbl_name in app_tables
]
Base.metadata.create_all(bind=engine, tables=tables)
with engine.begin() as connection:
    alembic_cfg = get_conf().ALEMBIC_CFG
    alembic_cfg.attributes["connection"] = connection
    command.upgrade(alembic_cfg, "head")


app = FastAPI()
app.add_route(
    "/graphql",
    GraphQLApp(
        schema=Schema(query=GqlQuery, mutation=GqlMutation), graphiql=True
    ),
)
