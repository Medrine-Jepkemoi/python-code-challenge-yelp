from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# creating the engine
engine = create_engine('sqlite:///customer.db')

# Creating the session
Session = sessionmaker(bind=engine)
session = Session()


# Creating the table
Base = declarative_base()

class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    given_name = Column(String)
    family_name = Column(String)

    def __init__ (self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name

    
    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f'{self._given_name}  {self._family_name}'

    @classmethod
    def all(cls):
        return session.query(cls).all()

        

