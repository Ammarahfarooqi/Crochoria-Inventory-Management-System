import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

def get_connection():

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return connection

def get_products():
    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return products

def add_product(name, category, price, stock):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
        INSERT INTO products (name, category, price, stock)
        VALUES (%s, %s, %s, %s)
    """

    values = (name, category, price, stock)

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

def delete_product(product_id):

    connection = get_connection()

    cursor = connection.cursor()

    query = "DELETE FROM products WHERE id = %s"

    cursor.execute(query, (product_id,))

    connection.commit()

    cursor.close()
    connection.close()

def update_product(product_id, name, category, price, stock):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
        UPDATE products
        SET name = %s,
            category = %s,
            price = %s,
            stock = %s
        WHERE id = %s
    """

    values = (name, category, price, stock, product_id)

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()

def get_product(product_id):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM products WHERE id = %s"

    cursor.execute(query, (product_id,))

    product = cursor.fetchone()

    cursor.close()
    connection.close()

    return product

def search_products(search_term):

    connection = get_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT * FROM products
        WHERE name LIKE %s
        OR category LIKE %s
    """

    search_pattern = "%" + search_term + "%"

    cursor.execute(query, (search_pattern, search_pattern))

    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return products

def get_statistics():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM products")
    total_products = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM products WHERE stock <= 5")
    low_stock = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT category) FROM products")
    categories = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return total_products, low_stock, categories