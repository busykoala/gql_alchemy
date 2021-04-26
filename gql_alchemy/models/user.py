from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from gql_alchemy.database import Base


class User(Base):
    __tablename__ = "tbl_user"

    pk = Column(Integer, primary_key=True)
    given_name = Column(String(200), nullable=True)
    family_name = Column(String(200), nullable=True)
