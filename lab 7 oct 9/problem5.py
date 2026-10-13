# Problem 5: Count how many times each element repeats in a list.

def count_repetitions(elements):
    """Return a dictionary of each value and how often it appears."""
    counts = {}
    for element in elements:
        counts[element] = counts.get(element, 0) + 1
    return counts


if __name__ == "__main__":
    print(count_repetitions(["cat", "dog", "cat", "cow", "cow", "cow"]))
    print(count_repetitions([1, 5, 5, 5, 12, 12, 0, 0, 0, 0, 0, 0]))
    print(count_repetitions(["Infinity", "null", "Infinity", "null", "null"]))
