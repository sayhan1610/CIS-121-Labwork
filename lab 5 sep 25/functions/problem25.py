
def leg_counter(chickens, cows, pigs):
    return chickens * 2 + cows * 4 + pigs * 4


if __name__ == "__main__":
    c = int(input("Enter chickens: "))
    cows = int(input("Enter cows: "))
    p = int(input("Enter pigs: "))
    print(leg_counter(c, cows, p))
