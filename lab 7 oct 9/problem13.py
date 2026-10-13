# Problem 13: Calculate the total calories for a list of fruits.

calories = {"apple": 95, "banana": 105, "orange": 62, "grape": 3, "pear": 102}


def total_calories(fruits):
    """Add the calories for each valid fruit in the list."""
    total = 0
    for fruit in fruits:
        if fruit in calories:
            total += calories[fruit]
    return total


if __name__ == "__main__":
    print(total_calories(["apple", "banana", "orange"]))
    print(total_calories(["grape", "grape", "grape", "grape", "grape"]))
    print(total_calories(["banana", "pear", "apple"]))
