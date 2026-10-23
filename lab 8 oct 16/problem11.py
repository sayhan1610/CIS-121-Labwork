"""Generate a list of multiples."""


def list_of_multiples(num, length=5):
    """Return length multiples of num, starting with num."""
    if not isinstance(length, int) or isinstance(length, bool):
        raise TypeError("length must be an integer")
    if length < 0:
        raise ValueError("length cannot be negative")
    return [num * multiplier for multiplier in range(1, length + 1)]


if __name__ == "__main__":
    print(list_of_multiples(7, 5))
    print(list_of_multiples(12, 10))
    print(list_of_multiples(2))
    print(list_of_multiples(2, 3))
