
def hailstone_seq(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


if __name__ == "__main__":
    start = int(input("Enter a starting number: "))
    print(hailstone_seq(start))
