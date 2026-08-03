from product import Product
from inventory import Inventory
from menu import show_menu

inventory = Inventory()

inventory.load_products()


while True:
    show_menu()
    choice = int(input("Enter your choice : "))

    if choice == 5:

        print("Thank you for using Crochoria Inventory System!")
        break

    if choice == 1:

        prod_id = int(input("Enter Product ID : "))
        name = input("Enter product name : ")
        category = input("Enter product category : ")
        price = float(input("Enter  product price : "))
        stock = int(input("Enter stock : "))
        product = Product(prod_id, name, category, price, stock)
        inventory.add_product(product)
        inventory.save_products()
        print("\nProduct added successfully!\n")

    elif choice == 2:

        inventory.display_products()

    elif choice == 3:

        inventory.search_product()

    elif choice == 4:

        inventory.delete_product()
        inventory.save_products()

    else:
        print("\nInvalid Choice\n")