class Product:
    def __init__(self, prod_id, name, category, price, stock):
        self.prod_id = prod_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def display(self):
            print("ID : ", self.prod_id, "\nName : ", self.name, "\nCategory : ", self.category, "\nPrice : ", self.price, "\nStock : ", self.stock)