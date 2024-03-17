#!/usr/bin/python3
"""
   script to search database table for records of name passed as argument
   that is safe from an sql injection attack
"""
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
        cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                    (name,))
        rows = cur.fetchall()
    except MySQLdb.Error as e:
        print(f"MySQL Error {str(e):s}")

    for row in rows:
        print(f"{row}")

    cur.close()
    conn.close()
