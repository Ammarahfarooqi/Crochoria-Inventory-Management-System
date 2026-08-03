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

    def load_products(self):
        with open("products.txt") as f:
            for line in f:
                line = line.strip()
                data = line.split(",")
                product = Product(int(data[0]), data[1], data[2], float(data[3]), int(data[4]))
                self.add_product(product)

    def save_products(self):
        with open("products.txt", "w") as f:
            for item in self.products:
                f.write(str(item.prod_id) + "," + item.name + "," + item.category + "," + str(item.price) + "," + str(item.stock) + "\n")
            
