"""Return the positive factors of an integer."""


def find_factors(num=36):
    """Return all positive factors of num in ascending order."""
    if not isinstance(num, int) or isinstance(num, bool):
        raise TypeError("num must be an integer")
    if num == 0:
        raise ValueError("zero has infinitely many factors")

    number = abs(num)
    factors = []
    for candidate in range(1, number + 1):
        if number % candidate == 0:
            factors.append(candidate)
    return factors


if __name__ == "__main__":
    print(find_factors(12))
    print(find_factors(17))
    print(find_factors(36))
    print(find_factors())
