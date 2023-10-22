#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all rows
from the 'states' table.
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Access to the database and retrieve data from the 'states' table.
    """
    database = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                                    passwd=argv[2], db=argv[3])
    cursorr = database.cursor()
    cursorr.execute("SELECT * FROM states")
    rows = cursorr.fetchall()
    for row in rows:
        print(row)
