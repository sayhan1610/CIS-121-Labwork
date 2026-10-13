# Problem 7: Return the single unique number in a list.

def find_unique(numbers):
    """Return the value that appears only once in the list."""
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    for number, count in counts.items():
        if count == 1:
            return number
    return None


if __name__ == "__main__":
    print(find_unique([1, 2, 2, 3, 3, 4, 4]))
    print(find_unique([7, 8, 8, 9, 9, 10, 10]))
    print(find_unique([5, 6, 6, 7, 7, 8, 8, 5, 9]))
