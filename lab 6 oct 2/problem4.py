# Problem 4: Return every odd number between two integers (inclusive).

def odd(smaller_num, larger_num):
    """Return all odd numbers from smaller_num to larger_num."""
    start, end = sorted((smaller_num, larger_num))
    if start % 2 == 0:
        start += 1
    return list(range(start, end + 1, 2))


if __name__ == "__main__":
    print(odd(37, 1050))
    print(odd(1, 2000))
    print(odd(50, 199))
