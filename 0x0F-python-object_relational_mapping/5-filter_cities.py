#!/usr/bin/python3
"""
This script connects to a MySQL database, retrieves the names of cities
in a specified state (case-sensitive), and orders the results by 'id'
in ascending order using parameterized queries.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Main function to access the database and retrieve city names in a
    specified state.
    """

    database = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                               passwd=argv[2], db=argv[3])

    with database.cursor() as cursor:
        cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })
        rows = cursor.fetchall()
    if rows is not None:
        print(", ".join([row[1] for row in rows]))
