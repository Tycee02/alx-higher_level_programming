#!/usr/bin/python3
"""List all cities from the db by given state
Username, password, database name, and state name given as user args
Can only use execute() once
Sort ascending order by cities.id
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
    cmd = """ SELECT cities.id, cities.name, states.name
          FROM cities
          JOIN states ON cities.state_id = states.id
          WHERE states.name = %s
          ORDER BY cities.id ASC
          """
    cur.execute(cmd)
    allCities = cur.fetchall()

    for city in  allCities:
        print(city)

    cur.close()
    db.close()
