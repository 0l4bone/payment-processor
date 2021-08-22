import db

from sqlalchemy import Column, Integer, String


class Customer(db.Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Customer({self.name})'

    def __str__(self):
        return self.name