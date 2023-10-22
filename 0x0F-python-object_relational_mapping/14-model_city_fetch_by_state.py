#!/usr/bin/python3
"""
This script connects to a MySQL database, retrieves information about
cities and their associated states, and prints the results.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database, retrieve information about cities and their
    associated states, and print the results.
    """
    database = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(database)
    Session = sessionmaker(bind=eng)
    sess = Session()
    que = sess.query(City, State).join(State)
    for _c, _s in que.all():
        print("{}: ({:d}) {}".format(_s.name, _c.id, _c.name))
    sess.commit()
    sess.close()
