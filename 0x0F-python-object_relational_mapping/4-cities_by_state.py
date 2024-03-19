#!/usr/bin/python3
"""List all cities from a given db sorted in ascending order by id
Username, password, and database names are given as user args
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM cities ORDER BY id ASC")
    allCities = cur.fetchall()

    for cities in allCities:
        print(cities)

    cur.close()
    db.close()
