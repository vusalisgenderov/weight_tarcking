from pydantic import BaseModel
from datetime import date

class UserCreateSchema(BaseModel):
    username:str
    password:str
    height:int
    class Config:
        extra="forbid"


class UserCreateWeightschema(BaseModel):
    username:str
    weight:float
    date:date
    class Config:
        extra="forbid"
