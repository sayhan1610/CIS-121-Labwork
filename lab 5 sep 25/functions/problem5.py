
from random import randint


def toss_coin(guess):
    value = randint(0, 1)
    return "Correct!" if guess == value else "Incorrect!"


if __name__ == "__main__":
    user_guess = int(input("Enter 0 for heads or 1 for tails: "))
    print(toss_coin(user_guess))
