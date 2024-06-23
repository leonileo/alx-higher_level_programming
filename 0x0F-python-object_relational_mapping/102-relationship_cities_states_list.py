#!/usr/bin/python3
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import sys
"""
    Module that performs MySQL query through MySQLAlchemy.
"""

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
