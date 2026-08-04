from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self):
        try:
            prod_id = int(input("Enter Product ID : "))
            name = input("Enter product name : ")
            category = input("Enter product category : ")
            price = float(input("Enter product price : "))
            stock = int(input("Enter stock : "))
        except ValueError:
            print("\nInvalid input. Product ID and Stock must be integers, Price must be a number.\n")
            return False

        for item in self.products:
            if prod_id == item.prod_id:
                print("\nProduct ID already exists.\n")
                return False
        product = Product(prod_id, name, category, price, stock)
        self.products.append(product)
        print("\nProduct added successfully!\n")
        return True

    def display_products(self):
        if len(self.products) == 0:
            print("\nNo products available\n")
        else:
            for item in self.products:
                item.display()

    def search_product(self): 
        product_id = int(input("Enter Product ID : "))
        found = False
        for item in self.products:
            if product_id == item.prod_id:
                found = True
                print("\nProduct found successfully!\n")
                item.display()
                break
        if found == False:
            print("\nProduct not found.\n")

    def delete_product(self):
        product_id = int(input("Enter Product ID : "))
        found = False
        for item in self.products:
            if product_id == item.prod_id:
                found = True
                self.products.remove(item)
                print("\nProduct deleted successfully!\n")
                break
        if found == False:
            print("\nProduct not found.\n")

    def update_product(self):
        product_id = int(input("Enter Product ID : "))
        found = False
        for item in self.products:
            if product_id == item.prod_id:
                found = True
                print("\nCurrent Product Details :\n")
                item.display()
                item.price = float(input("Enter new price : "))
                item.stock = int(input("Enter new stock : "))
                print("\nProduct updated successfully:\n")
                item.display()
                break
        if found == False:
            print("\nProduct not found.\n")

    def load_products(self):
        try:
            with open("products.txt") as f:
                for line in f:
                    line = line.strip()
                    data = line.split(",")
                    product = Product(int(data[0]), data[1], data[2], float(data[3]), int(data[4]))
                    self.products.append(product)
        except FileNotFoundError:
            print("\nNo saved products found. Starting with an empty inventory.\n")
            return 

    def save_products(self):
        with open("products.txt", "w") as f:
            for item in self.products:
                f.write(str(item.prod_id) + "," + item.name + "," + item.category + "," + str(item.price) + "," + str(item.stock) + "\n")
            
