
# from db.database import get_session
# from db import tables

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from context import db
from db import tables
#Create sqlite engine instance
engine=  create_engine('postgresql://postgre:root@localhost:5432/postgres')

#Create declaritive base meta instance
Base = declarative_base()
#Create session local class for session maker
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

def get_session():
    session = SessionLocal()
    try:
        yield session 
    finally:
        session.close()

session = get_session()
query = session.query(tables.Client)
result = query.first()
print(result)