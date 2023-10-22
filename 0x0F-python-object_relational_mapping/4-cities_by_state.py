#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves information about
 cities and their associated states.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Main function to access the database and retrieve city and state
    information.
    """

    database = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                               passwd=argv[2], db=argv[3])

    with database.cursor() as cursor:
        cursor.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """)

        rows = cursor.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
