#!/usr/bin/python3
"""
This script connects to a MySQL database, retrieves the first State object
ordered by ID, and prints its information.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database, retrieve the first State object ordered by
    ID, and print its information.
    """
    database = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(database)
    Session = sessionmaker(bind=eng)
    session = Session()
    inst = session.query(State).order_by(State.id).first()
    if inst is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(inst.id, inst.name))
