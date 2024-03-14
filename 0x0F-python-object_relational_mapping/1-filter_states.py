#!/usr/bin/python3
""" selects from table states all states whose name starts with N """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    host = "localhost"
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    port = 3306

    try:
        conn = MySQLdb.connect(host, user, passwd, db, port)
        cur = conn.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print(f"MySQL Error {str(e):s}")

    for row in rows:
        print(f"{row}")
