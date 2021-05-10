from sqlalchemy import Column, Integer, String, Float
from database import Base
from Utils.utils import ToDict
from Model.cart_model import Cart
from sqlalchemy.orm import sessionmaker, relationship,backref, joinedload

class Product(Base, ToDict):
  __tablename__ = 'product'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  description = Column(String)
  image = Column(String)
  price = Column(Float)
  stock = Column(Integer)

  productos_carrito = relationship("Cart",  back_populates="product", cascade="all, delete")

  def __init__(self, name, description, image, price, stock):
      self.name = name
      self.description = description
      self.image = image
      self.price = price
      self.stock = stock