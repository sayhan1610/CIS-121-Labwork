
from random import randint


def guess_num(guess):
    guess = guess.lower()
    value = randint(0, 9)
    result = "even" if value % 2 == 0 else "odd"
    return "Correct!" if guess == result else "Incorrect!"


if __name__ == "__main__":
    user_guess = input("Enter odd or even: ")
    print(guess_num(user_guess))
