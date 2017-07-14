from sqlalchemy import Column, Integer, String
from selectio.database import Base

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)  # e.g. 1, 2, 3, 4
    first_name = Column(String(50))         # e.g. Frank, Nick
    last_name = Column(String(50))          # e.g. Matranga
    nickname = Column(String(30))           # e.g. Nick
    title = Column(String(30))              # e.g. Mr., Mrs., Fr., Dr.
    relation = Column(String(50))           # Relation to me e.g. self, brother, friend, classmate
    gender = Column(String(10))             # Male, Female
    description = Column(String(250))                   # e.g. 17, 54, 79

    def __init__(self, first_name=None, last_name=None, nickname=None, title=None, relation=None, gender=None, description=None):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.relation = relation
        self.gender = gender
        self.description = description

    def __repr__(self):
        return '<User %r %r %r (%r)>' % (self.title, self.first_name, self.last_name, self.relation)