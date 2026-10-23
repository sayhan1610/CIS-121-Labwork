"""Return three numbers in descending order without sorting built-ins."""


def descending_order(num1, num2=15, num3=5):
    """Return the arguments in descending order."""
    first, second, third = num1, num2, num3

    if first < second:
        first, second = second, first
    if second < third:
        second, third = third, second
    if first < second:
        first, second = second, first

    return [first, second, third]


if __name__ == "__main__":
    print(descending_order(2, 3, 1))
    print(descending_order(10))
    print(descending_order(2, 45))
