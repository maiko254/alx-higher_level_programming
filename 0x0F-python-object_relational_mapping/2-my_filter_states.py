#!/usr/bin/python3
""" script to search database table for records of name passed as argument """
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
        q = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
                name)
        cur.execute(q)
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print(f"MySQL Error {str(e):s}")

    for row in rows:
        print(row)

    cur.close()
    conn.close()
