from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# creating the engine
engine = create_engine('sqlite:///restaurant.db')

# Creating the session
Session = sessionmaker(bind=engine)
session = Session()


# Creating the table
Base = declarative_base()

class Restaurant(Base):
    __tabelname__ = "restaurant"

    restaurant_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self._name = name

    # getter for Restaurant name()
    @property
    def name(self):
        return self._name
