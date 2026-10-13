# Problem 17: Return items you can afford from a dictionary of item prices.

def items_purchase(store, wallet):
    """Return the names of items whose prices are less than or equal to wallet."""
    affordable = []
    for item, price in store.items():
        if price <= wallet:
            affordable.append(item)
    return sorted(affordable)


if __name__ == "__main__":
    print(items_purchase({"Water": 1, "Bread": 3, "TV": 1000}, 300))
    print(items_purchase({"Apple": 4, "Pan": 100, "Spoon": 2}, 100))
    print(items_purchase({"Phone": 999, "Laptop": 5000, "PC": 1200}, 1))
