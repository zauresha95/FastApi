from sqlalchemy.orm import Session

"""
Session manages persistence operations for ORM-mapped objects.
Let's just refer to it as a database session for simplicity
"""

from models import Client

def create_client(db:Session, name, email, phone):
    """
    function to create a client model object
    """
    # create friend instance 
    new_client= Client(name, email, phone)
    #place object in the database session
    db.add(new_client)
    #commit your instance to the database
    db.commit()
    #reefresh the attributes of the given instance
    db.refresh(new_client)
    return new_client