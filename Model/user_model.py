from sqlalchemy import Column, Integer, String
from database import Base
from Utils.utils import ToDict
from Model.cart_model import Cart
from sqlalchemy.orm import sessionmaker, relationship,backref, joinedload

class User(Base, ToDict):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True)
  username = Column(String, unique = True)
  firstname = Column(String)
  lastname = Column(String)
  password = Column(String)

  productos_carrito = relationship("Cart",  back_populates="user", cascade="all, delete")

  def __init__(self, username, firstname, lastname, password):
    self.username = username
    self.firstname = firstname
    self.lastname = lastname
    self.password = password