#!/usr/bin/python3
"""
   lists State object with the name passed as argument to the script from
   the database a using sqlalchemy
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import select


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    stmt = select(State)
    states = session.execute(stmt).all()
    found = 1
    for state in states:
        if state[0].name == argv[4]:
            print(f"{state[0].id}")
            found = 0
    if found == 1:
        print("Not found")
