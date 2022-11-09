import dataclasses
from pydantic import BaseModel,Field
from datetime import date

class Client (BaseModel):
    name: str
    email: str#Field(regex='(\w|\.)+\@+[a-zA-Z]+\.[a-zA-Z]+', description="Allow email") #
    phone: int
    created: date
    updated: date
