#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # get the args
    username, password, db = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password, database=db, port=3306)

    cursor = db.cursor();
    query = "SELECT cities.id, cities.name, states.name FROM cities\
    INNER JOIN states ON cities.state_id = states.id\
    ORDER BY cities.id ASC;";

    cursor.execute(query);
    res = cursor.fetchall();

    for result in res:
        print(result)

    cursor.close()
    db.close()
