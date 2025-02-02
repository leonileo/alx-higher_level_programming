#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    # retreving args
    username, password, database, state_name = sys.argv[1:5]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Construct the query (Warning: Using .format() can lead to SQL Injection)
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)

    # Execute the query
    cur.execute(query)

    # Fetch all results
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()
    
