from sqlalchemy import Column, Integer, String, DateTime
from database import Base

from sqlalchemy.sql import func

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer,primary_key=True)
    name = Column(String(200)) # TODO не более 200 символов, кодировка UTF-8) , 
    email = Column(String(200)) #re.match('(\w|\.)+\@+[a-zA-Z]+\.[a-zA-Z]+','za.ure@mail.ru') # TODO(обеспечить валидацию формата email адресов), 
    phone = Column(Integer)  # re.match('7[0-9]+','71122') TODO (только числовые данные [прим 70098737475]), 
    created = Column(DateTime(), server_default = func.now())  # TODO (при создании обхекта - текущая дата добавляется автоматически, [единоразово]),  (подсказка: auto_now)
    updated = Column(DateTime(), server_default = func.now())  #(при обновлении обхекта - текущая дата добавляется автоматически), 
