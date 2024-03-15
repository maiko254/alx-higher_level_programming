#!/usr/bin/python3
""" select and displays all cities of a state from the database """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    host = "localhost"
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    port = 3306
    name = argv[4]

    try:
        conn = MySQLdb.connect(host, user, passwd, db, port)
        cur = conn.cursor()
        cur.execute("SELECT cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print(f"MySQL Error {str(e):s}")

    cities = []
    for row in rows:
        if row[1] == name:
            cities.append(row[0])

    print(", ".join(cities))

    cur.close()
    conn.close()
