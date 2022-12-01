from datetime import datetime
from fastapi import FastAPI, Depends, status, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import uvicorn
from context import db
from db import schemas, tables
from db.database import Base, engine, get_session

#This will create db if it doesn't alreasy exist 
Base.metadata.create_all(engine)
        
app = FastAPI()

@app.get("/{id}")
def getItem(id:int, session: Session = Depends(get_session)):
    try:
        item = session.query(tables.Client).get(id)#.all()
        if item:
            return item
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "Record not found"})
    except:
        session.rollback()
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": ''})

@app.post("/")
def addItem(client:schemas.Client, response: Response, session: Session = Depends(get_session)):
    try:
        item = tables.Client(
                                name = client.name,
                                email = client.email,
                                phone = client.phone
                                )
        session.add (item)
        session.commit()
        session.refresh(item)
        response.status_code = status.HTTP_201_CREATED
        return item
            #return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "Data is not correct"})
    except IntegrityError:
        session.rollback()
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": 'IntegrityError'})
    except TypeError:
        session.rollback()
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": 'TypeError'})
    except Exception as exc:
        print(exc)

@app.put("/{id}")
def updateItem(id:int,item:schemas.Client,response: Response, session: Session = Depends(get_session)):
    try:
        itemObject = session.query(tables.Client).get(id)
        if itemObject is not None:
            itemObject.name = item.name
            itemObject.email = item.email
            itemObject.phone = item.phone
            itemObject.updated = datetime.now()

            session.commit()
            response.status_code = status.HTTP_204_NO_CONTENT
            return itemObject
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "Record not found"})
    except:
        session.rollback()
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": ''})

@app.patch("/{id}")
def updatePartItem(id:int,item:schemas.Client,response: Response, session: Session = Depends(get_session)):
    try:
        itemObject = session.query(tables.Client).get(id)
        if not itemObject:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": ''})
        item_data = item.dict(exclude_unset=True)
        for key, value in item_data.items():
            setattr(itemObject, key, value)
        itemObject.updated = datetime.now()
        session.add(itemObject)
        session.commit()
        session.refresh(itemObject)

        response.status_code = status.HTTP_204_NO_CONTENT
        return itemObject
    except TypeError: # TODO 
        session.rollback()
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": ''}) # TODO 


@app.delete("/{id}")
def deleteItem(id:int, response: Response, session = Depends(get_session)):
    try:
        itemObject = session.query(tables.Client).get(id)
        if itemObject is not None:
            itemObject = session.query(tables.Client).get(id)
            session.delete(itemObject)
            session.commit()
            session.close()
            response.status_code = status.HTTP_204_NO_CONTENT
            return 'Item was deleted'
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "Record not found"})
    except:
        session.rollback()
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": ''})

if __name__ == '__main__':
    uvicorn.run("server.main:app", host="127.0.0.1", port=8000, reload=True)
    # log_level="debug", 
    #            workers=1, limit_concurrency=1, limit_max_requests=1)