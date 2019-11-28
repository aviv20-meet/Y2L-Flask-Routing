from flask import Flask, request, redirect, url_for, render_template 
from flask import session as login_session
from databases import get_table, add_to_cart, get_cart,get_product
app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

@app.route("/")
def home():
	return render_template("home.html")


@app.route("/store" , methods = ['GET', 'POST'])
def store():
	return render_template("store.html", products = get_table() )

@app.route("/add_to_cart/<id>")
def add_to_cartf(id):
	add_to_cart(id)
	return render_template("cart.html")



@app.route("/cart")
def cart():
	cart_items = []
	for i in get_cart():
		cart_items.append(get_product(i).id)

	return render_template("cart.html", cart_items = cart_items)

if __name__ == '__main__':
    app.run(debug=True)