from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from Utils.utils import ToDict
from database import get_db_session
from sqlalchemy.orm import sessionmaker, relationship,backref, joinedload
# from Model.user_model import User
# from Model.product_model import Product

class Cart(Base, ToDict):
  __tablename__ = 'cart'
  id = Column(Integer, primary_key=True)
  product_id = Column(Integer, ForeignKey('product.id'))
  user_id = Column(Integer, ForeignKey('user.id'), )
  created = Column(Integer) #yyyymmdd24hhMMss

  product = relationship("Product", back_populates="productos_carrito")
  user = relationship("User", back_populates="productos_carrito")

  def __init__(self, product_id, user_id, created):
    self.product_id = product_id
    self.user_id = user_id
    self.created = created