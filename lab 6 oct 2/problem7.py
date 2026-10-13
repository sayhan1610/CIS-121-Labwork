# Problem 7: Return three integers in ascending order without using min/max/sort.

def ascending_order(num1, num2, num3):
    """Sort three numbers in ascending order."""
    values = [num1, num2, num3]
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[j] < values[i]:
                values[i], values[j] = values[j], values[i]
    return values


if __name__ == "__main__":
    print(ascending_order(2, 3, 1))
    print(ascending_order(10, 1, 25))
    print(ascending_order(2, 45, 4))
