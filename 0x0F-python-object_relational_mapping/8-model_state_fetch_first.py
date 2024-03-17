#!/usr/bin/python3
""" lists the first State objects from the database using sqlalchemy """
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
    stmt = select(State).order_by(State.id)
    states = session.execute(stmt).first()
    if states:
        print(f"{states[0].id}: {states[0].name}")
    else:
        print('Nothing')
