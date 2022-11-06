from fastapi import FastAPI, Depends, status, Response
from fastapi.responses import JSONResponse
from FastApi.app import schemas
from FastApi.app import models
from FastApi.app.check_data import Check_Client
from FastApi.app.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import unittest
import requests
#This will create db if it doesn't alreasy exist 
Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session 
    finally:
        session.close()
        
app = FastAPI()

@app.get("/{id}")
def getItem(id:int, session: Session = Depends(get_session)):
    
    item = session.query(models.Client).get(id)#.all()
    if item:
        return item
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "Record not found"})

@app.post("/")
def addItem(client:schemas.Client, response: Response, session: Session = Depends(get_session)):
    try:
        if Check_Client.check_email(client.email) :#and Check_Client.check_phone(client.phone):
            item = models.Client(
                                name = client.name,
                                email = client.email,
                                phone = client.phone,
                                created = client.created,
                                updated = client.updated
                                )
            session.add (item)
            session.commit()
            session.refresh(item)
            response.status_code = status.HTTP_201_CREATED
            return item
        else:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "Data is not correct"})
    except IntegrityError:
        session.rollback()
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": 'IntegrityError'})
    
@app.put("/{id}")
def updateItem(id:int,item:schemas.Client,response: Response, session: Session = Depends(get_session)):
    itemObject = session.query(models.Client).get(id)
    print(itemObject)
    if itemObject is not None:
        itemObject.name = item.name
        itemObject.email = item.email
        itemObject.phone = item.phone
        #itemObject.updated = item.updated
        session.commit()
        response.status_code = status.HTTP_204_NO_CONTENT
        return itemObject
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "Record not found"})

@app.delete("/{id}")
def deleteItem(id:int, response: Response, session = Depends(get_session)):
    itemObject = session.query(models.Client).get(id)
    if itemObject is not None:
        itemObject = session.query(models.Client).get(id)
        session.delete(itemObject)
        session.commit()
        session.close()
        response.status_code = status.HTTP_204_NO_CONTENT
        return 'Item was deleted'
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "Record not found"})





class TestApp(unittest.TestCase):
   
    def setUp(self):
        self.data = {
                    "name": "zaure",
                    "email": "zaure@mail.ru",
                    "phone": 79991234567,
                    "created": "2022-10-09",
                    "updated": "2022-10-09"
                    }
        self.data2 = {
                    "name": "saule",
                    "email": "zaure@mail.ru",
                    "phone": 79991234567,
                    "created": "2022-10-09",
                    "updated": "2022-10-09"
                    }

    # def tearDown(self):
    #     self.widget.dispose()

    def test_1_post(self):
        res = requests.post("http://127.0.0.1:8000/", json = self.data)
        id = res.json().get('id')
        name = res.json().get('name')
        self.assertEqual(id,1)
        self.assertEqual(name,'zaure')
        self.assertEqual(res.status_code,201)

    def test_2_put(self):
        res = requests.put("http://127.0.0.1:8000/1", json = self.data2)
        #name = res.name
        #self.assertEqual(name,'saule')
        #print(res)
        self.assertEqual(res.status_code,204)

    def test_3_get(self):
        res = requests.get("http://127.0.0.1:8000/1")
        name = res.json().get('name')
        self.assertEqual(name,'saule')
        self.assertEqual(res.status_code,200)

    def test_4_delete(self):
        res = requests.delete("http://127.0.0.1:8000/1")
        self.assertEqual(res.status_code,204)


if __name__ == '__main__':
    unittest.main()
    #uvicorn main:app --reload