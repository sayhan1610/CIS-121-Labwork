"""Print the Hailstone sequence starting at a positive integer."""


def hailstone_seq(n=40):
    """Print successive Hailstone values through 1."""
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("n must be a positive integer")

    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    print(", ".join(str(value) for value in sequence))


if __name__ == "__main__":
    hailstone_seq(25)
    hailstone_seq(40)
    hailstone_seq()
