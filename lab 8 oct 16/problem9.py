"""Find all indices of a value in a list."""


def get_indices(values, value=0):
    """Return the indices where value occurs in values."""
    indices = []
    for index, item in enumerate(values):
        if item == value:
            indices.append(index)
    return indices


if __name__ == "__main__":
    print(get_indices([1, 0, 5, 0, 7]))
    print(get_indices([1, 5, 5, 2, 7], 7))
    print(get_indices([1, 5, 5, 2, 7]))
    print(get_indices([1, 5, 5, 2, 7], 5))
    print(get_indices([1, 5, 5, 2, 7], 8))
    print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
