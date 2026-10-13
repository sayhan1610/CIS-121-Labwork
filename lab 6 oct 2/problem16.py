# Problem 16: Determine whether the even or odd numbers sum to a larger total.

def war_of_numbers(numbers):
    """Return 'evens' if the even numbers sum more, otherwise 'odds'."""
    even_total = 0
    odd_total = 0
    for number in numbers:
        if number % 2 == 0:
            even_total += number
        else:
            odd_total += number
    if even_total > odd_total:
        return "evens"
    return "odds"


if __name__ == "__main__":
    print(war_of_numbers([2, 8, 7, 5]))
    print(war_of_numbers([12, 90, 75, 1, 1]))
    print(war_of_numbers([2, 10, 22, 243]))
