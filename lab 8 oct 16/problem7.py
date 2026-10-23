"""Return three numbers in ascending order without sorting built-ins."""


def ascending_order(num1, num2=5, num3=25):
    """Return the arguments in ascending order."""
    first, second, third = num1, num2, num3

    if first > second:
        first, second = second, first
    if second > third:
        second, third = third, second
    if first > second:
        first, second = second, first

    return [first, second, third]


if __name__ == "__main__":
    print(ascending_order(2, 3, 1))
    print(ascending_order(10, 1))
    print(ascending_order(50))
