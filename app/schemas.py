import dataclasses
from pydantic import BaseModel
from datetime import date

class Client (BaseModel):
    name: str
    email: str
    phone: int
    created: date
    updated: date
