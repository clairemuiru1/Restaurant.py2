from sqlalchemy import create_engine, desc
from sqlalchemy import (Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///restaurant.db')

Base = declarative_base()

class Customer(Base):
    __tablename__ =  'customers'
    id = Column(Integer(),primary_key=True)
    name = Column(String)
    price = Column(Integer)

def __repr__(self):
    return f"Customer {self.id}:"\
       +f"{self.name}:"