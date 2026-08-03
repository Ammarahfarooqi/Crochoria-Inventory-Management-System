from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        for item in self.products:
            item.display()

    def search_product(self): 
        id = int(input("Enter Product ID : "))
        found = False
        for item in self.products:
            if id == item.prod_id:
                found = True
                print("\nProduct found successfully!\n")
                item.display()
                break
        if found == False:
            print("\nProduct not found.\n")

    def delete_product(self):
        id = int(input("Enter Product ID : "))
        found = False
        for item in self.products:
            if id == item.prod_id:
                found = True
                self.products.remove(item)
                break
        if found == False:
            print("\nProduct not found.\n")