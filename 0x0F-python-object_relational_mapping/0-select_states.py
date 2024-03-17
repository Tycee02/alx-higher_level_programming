#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa, the script should take 3 arguments
Script should connect to a MySQL server, and sorted i ascending ordee by states.id
"""

import sys
import MySQL

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER by id ASC")
    allStates = cur.fetchall()

    for state in allStates:
        print(state)

    cur.close()
    db.close()
    
    