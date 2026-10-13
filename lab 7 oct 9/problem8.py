# Problem 8: Return the two unique numbers in a list.

def return_unique(numbers):
    """Return the two values that each appear only once."""
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return [number for number, count in counts.items() if count == 1]


if __name__ == "__main__":
    print(return_unique([1, 9, 8, 8, 7, 6, 1, 6]))
    print(return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))
    print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))
