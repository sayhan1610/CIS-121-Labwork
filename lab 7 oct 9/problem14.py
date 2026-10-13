# Problem 14: Calculate the total cost of a recipe from a list of ingredients.

prices = {
    "flour": 2.50,
    "sugar": 1.80,
    "eggs": 3.00,
    "milk": 2.00,
    "butter": 2.75,
    "vanilla": 4.50,
    "chocolate": 5.00,
}


def total_cost(ingredients):
    """Add the prices of each valid ingredient in the list."""
    total = 0.0
    for ingredient in ingredients:
        if ingredient in prices:
            total += prices[ingredient]
    return total


if __name__ == "__main__":
    print(total_cost(["flour", "sugar", "eggs", "butter"]))
    print(total_cost(["milk", "vanilla", "chocolate"]))
    print(total_cost(["eggs", "eggs", "flour", "sugar"]))
