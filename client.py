from xmlrpc import server
import sqlalchemy as sa
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base

class Clients(Base):
    __tablename__ = 'clients'
    name = sa.Column(sa.String(200)) # TODO не более 200 символов, кодировка UTF-8) , 
    email = sa.Column(sa.String(200))  # TODO(обеспечить валидацию формата email адресов), 
    phone = sa.Column(sa.String(200))  # TODO (только числовые данные [прим 70098737475]), 
    created = sa.Column(sa.DateTime(), server_default = func.now())  # TODO (при создании обхекта - текущая дата добавляется автоматически, [единоразово]),  (подсказка: auto_now)
    updated = sa.Column(sa.DateTime(), server_default = func.now())  #(при обновлении обхекта - текущая дата добавляется автоматически), 
