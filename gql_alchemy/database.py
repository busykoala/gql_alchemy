from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from gql_alchemy.config import get_conf

engine = create_engine(
    get_conf().DATABASE_URI, connect_args={"check_same_thread": False}
)


db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()
