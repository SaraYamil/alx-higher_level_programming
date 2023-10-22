#!/usr/bin/python3
"""
This script connects to a MySQL database, adds a new State object (Louisiana)
to the database, and prints the ID of the newly added State object.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database, add a new State object (Louisiana), print its
    ID, and close the session.
    """
    database = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(database)
    Session = sessionmaker(bind=eng)
    sess = Session()
    lou_state = State(name='Louisiana')
    sess.add(lou_state)
    sess.commit()
    print('{0}'.format(lou_state.id))
    sess.close()
