from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
	__tablename__ = "products"
	id = Column(Integer, primary_key= True)
	name = Column(String)
	price = Column(Integer)
	picture_link = Column(String)
	description = Column(String)


class Cart(Base):
	__tablename__ = 'cart'
	id = Column(Integer, primary_key = True)
	productID = Column(String)
	