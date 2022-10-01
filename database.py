from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import create_session

engine = create_session('sqlite:///sqlite3')
Session = sessionmaker(engine)
def get_session() -> Session():
    return Session()