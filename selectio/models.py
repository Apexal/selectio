from sqlalchemy import Column, Integer, String
from selectio.database import Base

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)  # e.g. 1, 2, 3, 4
    first_name = Column(String(50))         # e.g. Frank, Nick
    last_name = Column(String(50))          # e.g. Matranga
    title = Column(String(30))              # e.g. Mr., Mrs., Fr., Dr.
    relation = Column(String(50))           # Relation to me e.g. self, brother, friend, classmate
    gender = Column(String(10))             # Male, Female
    age = Column(Integer)                   # e.g. 17, 54, 79

    def __init__(self, first_name=None, last_name=None, title=None, relation=None, gender=None, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.relation = relation
        self.gender = gender
        self.age = age

    def __repr__(self):
        return '<User %r %r %r (%r)>' % (self.title, self.first_name, self.last_name, self.relation)