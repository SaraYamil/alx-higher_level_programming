#!/usr/bin/python3
"""
This script connects to a MySQL database, searches for a State object with
a specific name, and prints its ID if found.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database, search for a State object by name, and print its
    ID if found.
    """
    database = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(database)
    sess = sessionmaker(bind=eng)
    session = sess()
    inst = session.query(State).filter(State.name == argv[4]).first()
    if inst is None:
        print('Not found')
    else:
        print('{0}'.format(inst.id))
