class Inventory:
    def __init__(self):
        self.products = []
    def add_product(self, product):
        self.products.append(product)
    def display_product(self):
        for item in self.products:
            print("ID : ", item.prod_id, "\nName : ", item.name, "\nCategory : ", item.category, "\nPrice : ", item.price, "\nStock : ", item.stock)
            
