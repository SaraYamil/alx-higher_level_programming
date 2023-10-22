#!/usr/bin/python3
"""
This script connects to a MySQL database, retrieves rows from the 'states'
table where the name starts with 'N' (case-sensitive), and orders the results
by 'id' in ascending order.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and retrieve states whose names start with 'N'
    in ascending order.
    """
    database = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                               passwd=argv[2], db=argv[3])

    cursor = database.cursor()
    cursor.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
