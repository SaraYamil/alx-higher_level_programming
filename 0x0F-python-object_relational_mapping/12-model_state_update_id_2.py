#!/usr/bin/python3
"""
This script connects to a MySQL database, updates the name of a State
object with ID 2 to 'New Mexico',
and commits the changes to the database.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database, update the name of a State object with ID 2 to
    'New Mexico', and commit the changes to the database.
    """
    database = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(database)
    Session = sessionmaker(bind=eng)
    sess = Session()
    ari_state = sess.query(State).filter(State.id == '2').first()
    ari_state.name = 'New Mexico'
    sess.commit()
    sess.close()
