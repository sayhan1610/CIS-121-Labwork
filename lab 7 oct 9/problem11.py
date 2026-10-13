# Problem 11: Return the total number of products sold from a dictionary.

def total_sales(sales):
    """Return the sum of the values in the sales dictionary."""
    return sum(sales.values())


if __name__ == "__main__":
    print(total_sales({"Laptop": 5, "Phone": 10, "Tablet": 3}))
    print(total_sales({"Shoes": 20, "Hats": 15, "Jackets": 10}))
    print(total_sales({"Book": 1, "Pen": 2, "Notebook": 1}))
