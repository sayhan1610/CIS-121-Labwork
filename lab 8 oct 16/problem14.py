"""Identify and collect two-digit integers."""


def is_two_digit_number(num):
    """Return whether num is in [-99, -10] or [10, 99]."""
    return -99 <= num <= -10 or 10 <= num <= 99


def report_two_digit_numbers(numbers):
    """Return all two-digit integers, preserving order and duplicates."""
    two_digit_numbers = []
    for num in numbers:
        if is_two_digit_number(num):
            two_digit_numbers.append(num)
    return two_digit_numbers


if __name__ == "__main__":
    print(report_two_digit_numbers([100, 57, 12, 1]))
    print(report_two_digit_numbers([121, 36, -19, -6, 0, 21]))
    print(report_two_digit_numbers([100, 7, 8437]))
