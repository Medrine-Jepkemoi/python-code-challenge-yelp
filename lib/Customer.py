from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from Review import Review

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
        self._given_name = given_name
        self._family_name = family_name

    # getter and setter for given_name()
    @property
    def given_name(self):
        return self._given_name

    def given_name(self, value):
        self._given_name = value

    # getter and setter for family_name()
    @property
    def family_name(self):
        return self._family_name

    def family_name(self, value):
        self._family_name = value

    # getter for full_name()
    @property
    def full_name(self):
        return f'{self._given_name}  {self._family_name}'

    # returns **all** of the customer instances
    @classmethod
    def all(cls):
        return session.query(cls).all()

    # returns a list of all reviews for that restaurant
    def restaurants(self):
        unique_restaurant = set()
        for review in self.reviews:
            unique_restaurant.add(review.restaurant)
        return list(unique_restaurant)

    # given a **restaurant object** and a star rating (as an integer), creates a new review and associates it with that customer and restaurant
    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        session.add(new_review)
        session.commit()

