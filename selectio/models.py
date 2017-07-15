from sqlalchemy import Column, Integer, String, DateTime, SmallInteger, Enum, ForeignKey
from sqlalchemy.orm import relationship
from selectio.database import Base
import enum
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

    traits = relationship('PersonTrait')

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

class QualityEnum(enum.Enum):
    positive = 1
    neutral = 0
    negative = -1

class PersonTrait(Base):
    __tablename__ = 'person_traits'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('persons.id'))
    name = Column(String(30))
    quality = Column(Enum(QualityEnum))
    weight = Column(SmallInteger)
    description = Column(String(300))