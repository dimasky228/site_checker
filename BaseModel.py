from pydantic import BaseModel


class UserInput(BaseModel):
    expression: str
