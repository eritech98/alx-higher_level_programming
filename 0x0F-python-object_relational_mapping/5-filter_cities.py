#!/usr/bin/python3

"""
Takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities LEFT JOIN states ON cities.state_id = states.id \
                WHERE states.name=%s \
                ORDER BY cities.id ASC;", (state,))
    rows = cur.fetchall()

    if not rows:
        print()
    else:
        for index, row in enumerate(rows):
            if index == len(rows) - 1:
                print(row[1])
            else:
                print(f'{row[1]}, ', end='')

    cur.close()
    db.close()
