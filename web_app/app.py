from flask import Flask, render_template, request, redirect
from database import (
    get_products,
    add_product,
    delete_product,
    get_product,
    update_product,
    search_products,
    get_statistics
)

app = Flask(__name__)

@app.route("/")
def home():

    products = get_products()

    total_products, low_stock, categories = get_statistics()

    return render_template(
        "index.html",
        products=products,
        total_products=total_products,
        low_stock=low_stock,
        categories=categories,
        search_term=""
    )

@app.route("/add-product", methods=["GET", "POST"])
def add_product_page():

    if request.method == "POST":

        name = request.form["name"]
        category = request.form["category"]
        price = request.form["price"]
        stock = request.form["stock"]

        add_product(name, category, price, stock)

        return redirect("/")

    return render_template("add_product.html")

@app.route("/delete-product/<int:product_id>")
def delete_product_page(product_id):

    delete_product(product_id)

    return redirect("/")

@app.route("/edit-product/<int:product_id>", methods=["GET", "POST"])
def edit_product_page(product_id):

    product = get_product(product_id)

    if request.method == "POST":

        name = request.form["name"]
        category = request.form["category"]
        price = request.form["price"]
        stock = request.form["stock"]

        update_product(
            product_id,
            name,
            category,
            price,
            stock
        )

        return redirect("/")

    return render_template(
        "edit_product.html",
        product=product
    )

@app.route("/search")
def search():

    search_term = request.args.get("q", "")

    if search_term:
        products = search_products(search_term)
    else:
        products = get_products()

    total_products, low_stock, categories = get_statistics()

    return render_template(
        "index.html",
        products=products,
        search_term=search_term,
        total_products=total_products,
        low_stock=low_stock,
        categories=categories
    )

if __name__ == "__main__":
    app.run(debug=True)

