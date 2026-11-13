# Problem 11: Product and ShoppingCart classes

# Part (a): Product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def display_details(self):
        print(f"Product: {self.name}")
        print(f"Price: ${self.price:.2f}")

    def __str__(self):
        return f"Product(name={self.name}, price=${self.price:.2f})"


# Part (b): ShoppingCart class
class ShoppingCart:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0.0
        for product in self.products:
            total += product.get_price()
        return total

    def __str__(self):
        return f"ShoppingCart(customer_id={self.customer_id})"


# Part (c): Demonstration
if __name__ == "__main__":
    cart = ShoppingCart("C-1024")
    product1 = Product("Notebook", 4.50)
    product2 = Product("Pen", 1.75)

    cart.add_product(product1)
    cart.add_product(product2)

    print(cart)
    print(product1)
    print(product2)
    print(f"Total: ${cart.calculate_total():.2f}")
