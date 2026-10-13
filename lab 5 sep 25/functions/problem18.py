
def find_factors(num):
    factors = []
    for value in range(1, num + 1):
        if num % value == 0:
            factors.append(value)
    return factors


if __name__ == "__main__":
    value = int(input("Enter a number: "))
    print(find_factors(value))
