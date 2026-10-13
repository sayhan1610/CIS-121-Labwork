# Problem 11: Find the largest odd number in a list or return -1.

def largest_odd(numbers):
    """Return the largest odd value or -1 if none exists."""
    largest = -1
    for number in numbers:
        if number % 2 != 0 and number > largest:
            largest = number
    return largest


if __name__ == "__main__":
    print(largest_odd([3, 7, 2, 1, 7, 9, 10, 13]))
    print(largest_odd([2, 4, 6, 8]))
    print(largest_odd([0, 19, 18973623]))
