#!/usr/bin/python3
"""Base module"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

Base.metadata.create_all(engine)


class State(Base):
    """State class"""
    __tablename__ = "states"
    id = Column('id', Integer, autoincrement=True, primary_key=True)
    name = Column('name', String(128))

    def __init__(self, name):
        self.name = name
