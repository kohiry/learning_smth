from enum import Enum
from pydantic import BaseModel


class BaseSchema(BaseModel):

    class Config:
        from_attributes = True


class HttpVerbs(Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"
