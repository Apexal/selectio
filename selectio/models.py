from sqlalchemy import Column, Integer, String
from selectio.database import Base

class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    title = Column(String(30))
    gender = Column(String(10))
    age = Column(Integer)

    def __init__(self, first_name=None, last_name=None, title=None):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title

    def __repr__(self):
        return '<User %r %r %r>' % (self.title, self.first_name, self.last_name)