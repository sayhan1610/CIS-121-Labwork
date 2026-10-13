# Problem 9: Add corresponding elements in two lists.

def add_lists(lyst1, lyst2):
    """Return a new list with sums of each matching element."""
    return [first + second for first, second in zip(lyst1, lyst2)]


if __name__ == "__main__":
    print(add_lists([1, 3, 3, 1], [4, 3, 6, 1]))
    print(add_lists([1, 8, 5, 0, -7], [0, -7, 4, 2, -6]))
    print(add_lists([1, 2], [-1, 1]))
