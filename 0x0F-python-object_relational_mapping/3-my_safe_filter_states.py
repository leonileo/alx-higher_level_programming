#!/usr/bin/python3
"""my safe filter states"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Retrive args"""
    username, password, database, state_name = sys.argv[1:5]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch and print all results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()
