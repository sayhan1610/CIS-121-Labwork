"""Count how many of three numbers share a value."""


def count_duplicates(num1=0, num2=0, num3=0):
    """Report the largest group of equal values among the three numbers."""
    if num1 == num2 == num3:
        return "There are 3 of the same number"
    if num1 == num2 or num1 == num3 or num2 == num3:
        return "There are 2 of the same number"
    return "Each number is unique"


if __name__ == "__main__":
    print(count_duplicates(2, 3, 2))
    print(count_duplicates(4, 4, 4))
    print(count_duplicates(1, 2, 3))
    print(count_duplicates(1))
    print(count_duplicates(0))
