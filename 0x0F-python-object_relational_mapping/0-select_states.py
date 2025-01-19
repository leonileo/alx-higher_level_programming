#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Retrieve command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query to retrieve all states, ordered by id
    query = "SELECT * FROM states ORDER BY id ASC;"
    cursor.execute(query)

    # Fetch all results
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close cursor and database connection

    
