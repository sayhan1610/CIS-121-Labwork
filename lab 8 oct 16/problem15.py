"""Identify negative odd integers in a list."""


def is_negative(num):
    """Return whether num is negative."""
    return num < 0


def is_odd(num):
    """Return whether num is odd."""
    return num % 2 != 0


def report_negative_odds(numbers):
    """Return values that are both negative and odd."""
    negative_odds = []
    for num in numbers:
        if is_negative(num) and is_odd(num):
            negative_odds.append(num)
    return negative_odds


if __name__ == "__main__":
    print(report_negative_odds([100, -57, 12, 1, -36, -15]))
    print(report_negative_odds([121, -101, 36, -19, -6, 0, 21, -1]))
    print(report_negative_odds([-100, 7, 8437]))
