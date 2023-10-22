#!/usr/bin/python3
"""
This script connects to a MySQL database, creates a new State object
(California) and a new City object (San Francisco), establishes a relationship
between them, and commits the changes to the database.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """
    Access the database, create a new State object (California) and a
    new City object (San Francisco), establish a relationship between
    them, and commit the changes to the database.
    """
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                        format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    sess = Session()
    st = sess.query(State).outerjoin(City).order_by(State.id, City.id).all()
    for state in st:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
