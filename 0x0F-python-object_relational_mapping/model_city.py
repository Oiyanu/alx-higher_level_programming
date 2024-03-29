#!/usr/bin/python3
"""a Python file similar to model_state.py named model_city.py, City class"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalhemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Class City"""

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullabale=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
