from multiprocessing.connection import Client
from sqlalchemy.orm import Session
from models import Client
Session.query(Client).all()