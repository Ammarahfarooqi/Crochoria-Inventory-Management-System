from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product_console(self):
        try:
            prod_id = int(input("Enter Product ID : "))
            if self.id_exists(prod_id):
                print("\nProduct ID already exists.\n")
                return False
            name = input("Enter Product Name : ")
            category = input("Enter Category : ")
            price = float(input("Enter Price : "))
            stock = int(input("Enter Stock : "))

        except ValueError:
            print("Invalid Input")
            return False

        product = Product(prod_id, name, category, price, stock)
        return self.add_product(product)
            

    def add_product(self, product):
        for item in self.products:
            if item.prod_id == product.prod_id:
                print("\nProduct ID already exists.\n")
                return False

        self.products.append(product)
        self.products.sort(key=lambda x: x.prod_id)
        print("\nProduct added successfully!\n")
        return True
    
    def id_exists(self, product_id):
        for item in self.products:
            if item.prod_id == product_id:
                return True
        return False

    def display_products(self):
        if len(self.products) == 0:
            print("\nNo products available\n")
        else:
            for item in sorted(self.products, key=lambda x: x.prod_id):
                item.display()

    def get_products(self):
        return self.products

    def search_product(self):
        while True:
            try :
                search = int(input("1. Search by ID OR 2. Search by name\nEnter your choice : ")) 
            except ValueError:
                print("\nEnter a valid choice\n")
                continue
            if search == 1:
                product_id = int(input("\nEnter Product ID : "))
                found = False
                for item in self.products:
                    if product_id == item.prod_id:
                        found = True
                        print("\nProduct found successfully!\n")
                        item.display()
                        break
                if found == False:
                    print("\nProduct not found.\n")
            elif search == 2:
                product_name = input("\nEnter Product Name : ")
                found = False
                for item in self.products:
                    if product_name.lower() == item.name.lower():
                        found = True
                        print("\nProduct found successfully!\n")
                        item.display()
                        break
                if found == False:
                    print("\nProduct not found.\n")
            else:
                print("\nEnter a valid no\n")

    def find_product_by_id(self, product_id):
        for item in self.products:
            if item.prod_id == product_id:
                return item
        return None

    def delete_product(self):
        product_id = int(input("Enter Product ID : "))
        found = False
        for item in self.products:
            if product_id == item.prod_id:
                found = True
                while True:
                    confirm = input("Are you sure want to delete? (Y/N) : ")
                    if confirm == 'y' or confirm == 'Y':
                        self.products.remove(item)
                        print("\nProduct deleted successfully!\n")
                        break
                    elif confirm == 'n' or confirm == 'N':
                        print("\nDeletion cancelled.\n")
                        break
                    else:
                        print("\nEnter valid choice\n")
        if found == False:
            print("\nProduct not found.\n")

    def delete_product_by_id(self, product_id):
        for item in self.products:
            if item.prod_id == product_id:
                self.products.remove(item)
                return True

        return False

    
    def update_product_by_id(self, product_id, price, stock):
        product = self.find_product_by_id(product_id)
        if product:
            product.price = price
            product.stock = stock
            return True
        return False

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



    def inventory_summary(self):
        total_products = len(self.products)
        total_stock = 0
        total_value = 0
        for item in self.products:
            total_stock += item.stock
            total_value += item.stock * item.price
        print("========== INVENTORY SUMMARY ==========\n")
        print("Total Products : ", total_products, "\nTotal Stock : ", total_stock, "\nInventory Value : ", total_value)


    def load_products(self):
        try:
            with open("products.txt") as f:
                for line in f:
                    line = line.strip()
                    data = line.split(",")
                    product = Product(int(data[0]), data[1], data[2], float(data[3]), int(data[4]))
                    self.products.append(product)
                    self.products.sort(key=lambda x: x.prod_id)
        except FileNotFoundError:
            print("\nNo saved products found. Starting with an empty inventory.\n")
            return 


    def save_products(self):
        with open("products.txt", "w") as f:
            for item in self.products:
                f.write(str(item.prod_id) + "," + item.name + "," + item.category + "," + str(item.price) + "," + str(item.stock) + "\n")
            
