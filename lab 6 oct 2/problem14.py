# Problem 14: Return a list of multiples of a number up to the given length.

def list_of_multiples(num, length):
    """Return a list of the first length multiples of num."""
    multiples = []
    current = num
    while len(multiples) < length:
        multiples.append(current)
        current += num
    return multiples


if __name__ == "__main__":
    print(list_of_multiples(7, 5))
    print(list_of_multiples(12, 10))
    print(list_of_multiples(17, 6))
