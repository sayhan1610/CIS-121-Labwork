# Problem 6: Return all factors of a given integer.

def find_factors(num):
    """Return every positive factor of num."""
    factors = []
    for value in range(1, num + 1):
        if num % value == 0:
            factors.append(value)
    return factors


if __name__ == "__main__":
    print(find_factors(12))
    print(find_factors(17))
    print(find_factors(36))
