#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    # retriving args
    username = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]

    # connecting to db
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=db_passwd, db=db_name)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;"
    cursor.execute(query)

    states = cursor.fetchall()
    for i in states:
        print(i)
    cursor.close()
    db.close()
