# Problem 13: Return the indices where an item appears in a list.

def get_indices(sequence, item):
    """Return all index positions where item appears."""
    indices = []
    for index, value in enumerate(sequence):
        if value == item:
            indices.append(index)
    return indices


if __name__ == "__main__":
    print(get_indices([1, 5, 5, 2, 7], 7))
    print(get_indices([1, 5, 5, 2, 7], 5))
    print(get_indices([1, 5, 5, 2, 7], 8))
    print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
