
def square_sum(num):
    if num < 0:
        return "unknown"
    total = 0
    for value in range(1, num + 1):
        total += value ** 2
    return total


if __name__ == "__main__":
    value = int(input("Enter a number: "))
    print(square_sum(value))
