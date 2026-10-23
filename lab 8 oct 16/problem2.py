"""(Game: Odd or Even) Write a function that lets the user guess whether a randomly generated number
is odd or even. The function randomly generates an integer between 0 and 9 (inclusive) and returns
whether the user’s guess is correct or incorrect. The argument for the function will be guess (the user’s
guess, either ” odd” or ” even”), if no argument is provided then the default guess should be even.
Hint: Use the following lines of code to create the function.
from random import randint
value = randint(0,9) #picks a random integer between 0-9 inclusive
Examples:
guess( ) → ” Correct!” (if random value is even) or ” Incorrect!” (if random value is odd)
guess( ” odd”)→ ” Correct!” (if random value is odd) or ” Incorrect!” (if random value is even)
guess( ” even”) → ” Correct!” (if random value is even) or ” Incorrect!” (if random value is odd)"""




from random import randint


def guess_number(guess="even"):
    """Return whether guess matches the parity of a random digit.

    The digit is from 0 through 9, and the default guess is "even".
    """
    if guess not in ("odd", "even"):
        raise ValueError("guess must be 'odd' or 'even'")

    value = randint(0, 9)
    is_even = value % 2 == 0
    if (guess == "even") == is_even:
        return "Correct!"
    return "Incorrect!"


if __name__ == "__main__":
    user_guess = input(
        "Guess if the number is odd or even (type 'odd' or 'even'): "
    ).lower()
    try:
        print(guess_number(user_guess))
    except ValueError as error:
        print(error)