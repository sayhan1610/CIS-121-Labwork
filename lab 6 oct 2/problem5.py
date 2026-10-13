# Problem 5: Create the hailstone sequence starting at n.

def hailstone_sequence(n):
    """Return the hailstone sequence from n until it reaches 1."""
    sequence = []
    current = n

    while current != 1:
        sequence.append(current)
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
    sequence.append(1)
    return sequence


if __name__ == "__main__":
    print(hailstone_sequence(25))
    print(hailstone_sequence(40))
