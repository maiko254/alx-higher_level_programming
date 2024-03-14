#!/usr/bin/python3
""" Script that lists States from a database using MySQLdb module """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    host = "localhost"
    port = 3306

    try:
        conn = MySQLdb.connect(host, user, passwd, db, port)
        c = conn.cursor()
        c.execute("SELECT * FROM states ORDER BY id ASC")
        rows = c.fetchall()
    except MySQLdb.Error as e:
        try:
            print(f"MySQL Error [{e.args[0]:d}]: {e.args[1]:s}")
        except IndexError:
            print(f"MySQL Error: {str(e):s}")

    for row in rows:
        print(f"{row}")

    c.close()
    conn.close()
