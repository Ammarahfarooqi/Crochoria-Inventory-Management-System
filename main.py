from product import Product
from inventory import Inventory

penguin = Product(1, "Penguin", "keychain", 850, 3)

inventory = Inventory()
inventory.add_product(penguin)
inventory.display_product()