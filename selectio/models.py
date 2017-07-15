from sqlalchemy import Column, Integer, String, DateTime
from selectio.database import Base
import datetime

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)  # e.g. 1, 2, 3, 4
    first_name = Column(String(50))         # e.g. Frank, Nick
    last_name = Column(String(50))          # e.g. Matranga
    nickname = Column(String(30))           # e.g. Nick
    relation = Column(String(50))           # e.g. self, brother, friend, classmate
    gender = Column(String(10))             # e.g. Male, Female
    description = Column(String(250))       # e.g. Coolest guy ever...

    added_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, first_name=None, last_name=None, nickname=None, relation=None, gender=None, description=None):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.relation = relation
        self.gender = gender
        self.description = description

    def __repr__(self):
        return '<User %r %r (%r)>' % (self.first_name, self.last_name, self.relation)
