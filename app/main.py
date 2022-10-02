#add this to main.py above the point where you initialized FastAPI
#import
import models
from db import engine

#create the database tables on app startup or reload
models.Base.metadata.create_all(bind=engine)

from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


from db import SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""
So that FastAPI knows that it has to treat a variable as a dependency, we will import Depends
"""
from fastapi import Depends
#import crud to give access to the operations that we defined
import crud
from sqlalchemy.orm import Session

#define endpoint
@app.post("/create_client")
def create_client(name:str, email:str, phone:str, db:Session = Depends(get_db)):
    client = crud.create_client(db=db, name=name, email=email, phone=phone)
##return object created
    return {"client": client}