# Problem 10: Find the largest even number in a list or return -1.

def largest_even(numbers):
    """Return the largest even value or -1 if none exists."""
    largest = -1
    for number in numbers:
        if number % 2 == 0 and number > largest:
            largest = number
    return largest


if __name__ == "__main__":
    print(largest_even([3, 7, 2, 1, 7, 9, 10, 13]))
    print(largest_even([1, 3, 5, 7]))
    print(largest_even([0, 19, 18973623]))
