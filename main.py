from product import Product
from inventory import Inventory
from menu import show_menu

inventory = Inventory()

inventory.load_products()


while True:
    show_menu()
    choice = int(input("Enter your choice : "))

    if choice == 6:

        print("Thank you for using Crochoria Inventory System!")
        break

    if choice == 1:

        if inventory.add_product():
            inventory.save_products()

    elif choice == 2:

        inventory.display_products()

    elif choice == 3:

        inventory.search_product()

    elif choice == 4:

        inventory.delete_product()
        inventory.save_products()

    elif choice == 5:
        inventory.update_product()
        inventory.save_products()

    else:
        print("\nInvalid Choice\n")