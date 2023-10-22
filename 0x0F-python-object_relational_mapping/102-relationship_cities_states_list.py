#!/usr/bin/python3
"""
This script connects to a MySQL database, retrieves information about cities
and their associated states, and prints the results.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    """
    Access the database, retrieve information about cities and their
    associated states, and print the results.
    """
    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                        format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)
    Session = sessionmaker(bind=eng)
    sess = Session()
    st = sess.query(State).join(City).order_by(City.id).all()
    for state in st:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
