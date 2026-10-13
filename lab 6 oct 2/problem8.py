# Problem 8: Return three integers in descending order without using min/max/sort.

def descending_order(num1, num2, num3):
    """Sort three numbers in descending order."""
    values = [num1, num2, num3]
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[j] > values[i]:
                values[i], values[j] = values[j], values[i]
    return values


if __name__ == "__main__":
    print(descending_order(2, 3, 1))
    print(descending_order(10, 1, 25))
    print(descending_order(2, 45, 4))
