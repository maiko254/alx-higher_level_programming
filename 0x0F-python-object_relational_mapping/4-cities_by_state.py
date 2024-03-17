#!/usr/bin/python3
""" selects and displays all cities in table cities from the database """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    host = "localhost"
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    port = 3306

    try:
        conn = MySQLdb.connect(host, user, passwd, db, port)
        cur = conn.cursor()
        cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                    JOIN states ON cities.state_id = states.id ORDER BY
                    cities.id ASC""")
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print(f"MySQL Error {str(e):s}")

    for row in rows:
        print(f"{row}")

    cur.close()
    conn.close()
