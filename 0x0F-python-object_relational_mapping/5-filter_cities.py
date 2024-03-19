#!/usr/bin/python3
"""Take the name of argument and list all cities of state
given the db in ascending order by id
Username, password, database name, and state name given as user args
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

    for city i  allCities:
        print(city)

    cur.close()
    db.close()