#!/usr/bin/python3
"""
This script connects to a MySQL database, deletes State objects whose
names contain 'a',
and commits the changes to the database.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database, delete State objects whose names contain 'a',
    and commit the changes to the database.
    """
    database = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(database)
    Session = sessionmaker(bind=eng)
    sess = Session()
    for instance in sess.query(State).filter(State.name.contains('a')):
        sess.delete(instance)
    sess.commit()
    sess.close()
