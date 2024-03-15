#!/usr/bin/python3
""" lists all State objects from the database using sqlalchemy """
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import select


if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}', pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    stmt = select(State).order_by(State.id)
    states = session.execute(stmt).all()
    for state in states:
        print(f"{state[0].id}: {state[0].name}")
