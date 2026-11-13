# Lab 12 Problem 10: ShoppingCart class
# Rubric focus: __add__ merges two carts by quantity and __str__ prints
# each item with its count.


class ShoppingCart:
    def __init__(self, items=None):
        # Use a dictionary where the key is the item and the value is the quantity.
        self.items = {} if items is None else dict(items)

    def add_item(self, item_name):
        # If the item already exists, increase the quantity; otherwise, set it to 1.
        if item_name in self.items:
            self.items[item_name] += 1
        else:
            self.items[item_name] = 1

    def __add__(self, other):
        # Add the quantities of matching items and keep the unique items too.
        if not isinstance(other, ShoppingCart):
            return NotImplemented

        merged = ShoppingCart(self.items)
        for item, quantity in other.items.items():
            if item in merged.items:
                merged.items[item] += quantity
            else:
                merged.items[item] = quantity
        return merged

    def __str__(self):
        # Print the cart as a human-readable list of item: quantity pairs.
        entries = [f"{item}: {quantity}" for item, quantity in self.items.items()]
        return "ShoppingCart({" + ", ".join(entries) + "})" if entries else "ShoppingCart({})"


if __name__ == "__main__":
    cart1 = ShoppingCart()
    cart2 = ShoppingCart()

    cart1.add_item("tea")
    cart1.add_item("energy drink")
    cart1.add_item("energy drink")

    cart2.add_item("energy drink")
    cart2.add_item("hat")
    cart2.add_item("energy drink")
    cart2.add_item("energy drink")

    combined = cart1 + cart2

    print("cart1:", cart1)
    print("cart2:", cart2)
    print("cart1 + cart2:", combined)
