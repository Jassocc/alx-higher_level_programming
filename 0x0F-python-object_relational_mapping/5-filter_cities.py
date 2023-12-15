#!/usr/bin/python3
"""
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM states \
                   INNER JOIN cities ON states.id = cities.state_id \
                   WHERE states.name LIKE %s \
                   ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cursor.fetchall()
    city_names = (row[0] for row in rows)
    print(', '.join("{:s}".format(name) for name in city_names))
    cursor.close()
    db.close()
