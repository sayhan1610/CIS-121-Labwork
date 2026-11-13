# Problem 12: MenuItem and Restaurant classes

# Part (a): MenuItem class
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def show_description(self):
        print(f"Item: {self.name}")
        print(f"Price: ${self.price:.2f}")

    def __str__(self):
        return f"MenuItem(name={self.name}, price=${self.price:.2f})"


# Part (b): Restaurant class
class Restaurant:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.menu_items = []

    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)

    def display_menu(self):
        print(f"{self.restaurant_name} menu:")
        for item in self.menu_items:
            print(f" - {item.name}: ${item.price:.2f}")

    def lunch_menu(self):
        print(f"{self.restaurant_name} lunch menu:")
        for item in self.menu_items:
            print(f" - {item.name}: ${item.price - 2:.2f}")

    def __str__(self):
        return f"Restaurant(name={self.restaurant_name})"


# Part (c): Demonstration
if __name__ == "__main__":
    restaurant = Restaurant("Cedar Grill")
    item1 = MenuItem("Burger", 12.50)
    item2 = MenuItem("Salad", 9.00)

    restaurant.add_menu_item(item1)
    restaurant.add_menu_item(item2)

    print(restaurant)
    print(item1)
    print(item2)
    restaurant.display_menu()
    restaurant.lunch_menu()
