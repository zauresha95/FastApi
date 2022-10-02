from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#define sqlite connection url
SQLALCHEMY_DATABASE_URL = "sqlite:///./clients_api.db"

# create new engine instance 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create sessionmaker 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import create_session

# engine = create_session('sqlite:///sqlite3')
# Session = sessionmaker(engine)
# def get_session() -> Session():
#     return Session()


# from fastapi import FastAPI, UploadFile, File, Form
# from fastapi.middleware.cors import CORSMiddleware
# from databases import Database

# database = Database("sqlite:///test.db")


# @app.on_event("startup")
# async def database_connect():
#     await database.connect()


# @app.on_event("shutdown")
# async def database_disconnect():
#     await database.disconnect()


# @app.post("/test")
# async def fetch_data(id: int):
#     query = "SELECT * FROM tablename WHERE ID={}".format(str(id))
#     results = await database.fetch_all(query=query)