from pydantic import BaseModel


class UserType(BaseModel):
    given_name: str
    family_name: str
