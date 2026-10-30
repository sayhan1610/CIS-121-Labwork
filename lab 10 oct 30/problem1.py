# Outcome 11: Define a class with initialized attributes and working accessors.
class Product:
    def __init__(self, name, price, quantity):
        # self stores the data on this particular Product object.
        self.name = name
        self.price = price
        self.quantity = quantity

    # Each getter reads an attribute; its setter updates that attribute.
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity


if __name__ == "__main__":
    # Create an instance and demonstrate reading its attributes.
    product = Product("Notebook", 2.50, 10)
    print(product.get_name(), product.get_price(), product.get_quantity())
