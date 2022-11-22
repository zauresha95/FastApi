from server.db.database import Base

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer,primary_key=True)
    name = Column(String(200),unique=True)
    email = Column(String(200))
    phone = Column(Integer)
    created = Column(DateTime(), server_default = func.now())
    updated = Column(DateTime(), server_default = func.now())
