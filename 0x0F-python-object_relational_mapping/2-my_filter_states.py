#!/usr/bin/python3

"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
It's safe from MySQL injections.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()

    cur.execute("SELECT id, name FROM states WHERE BINARY name = '{}' \
                ORDER BY states.id ASC".format(name))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
