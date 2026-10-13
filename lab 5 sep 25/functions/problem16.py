
def sum_loop():
    total = 0
    while True:
        num = int(input("Enter an integer (negative to stop): "))
        if num < 0:
            return total
        total += num


if __name__ == "__main__":
    print(sum_loop())
