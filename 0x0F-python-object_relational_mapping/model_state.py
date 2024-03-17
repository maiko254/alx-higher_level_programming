#!/usr/bin/python3
"""
   Defining class State to be mapped to table states in database
   using sqlalchemy
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """ Definition of class State to be linked to table states in MySQL """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
