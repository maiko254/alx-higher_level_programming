#!/usr/bin/python3
""" Defines class City to be mapped to table cities in the database """
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
