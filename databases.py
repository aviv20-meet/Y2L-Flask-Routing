from model import Base, Product, Cart


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_product(name, price, pic_link, des):
	product_object = Product(
		name,
		price,
		pic_link,
		des)
	session.add(product_object)
	session.commit()
def edit_product(id, name,price,pic_link,des):
	product_object = session.query(Product).filter_by(id = id).first()
	product_object.name = name
	product_object.price = price
	product_object.picture_link = pic_link
	product_object.description = des
	session.commit()

def delete_product(id):
	product_object = session.query(Product).filter_by(id = id).delete()
	session.commit()

def get_table():
	product_table = session.query(Product).all()
	return product_table

def get_product(id):
	product_object = session.query(Product).filter_by(id = id).first()
	return product_object

def add_to_cart(productID):
	cart_object = Cart(productID)
	session.add(cart_object)
	session.commit()