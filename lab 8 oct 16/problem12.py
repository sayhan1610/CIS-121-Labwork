"""
Write a function named is even that returns a boolean value which determines if an integer is even.
Write a second function named report evens that takes a list of integers and returns a new list containing
all the even numbers from the original list. Call the is even function as part of the report evens function.
report evens([4,3,12,16,8,9,25]) → [4,12,16,8]
report evens([6,100,3,12,16,6,9,100]) → [6,100,12,16,6,100]
report evens([3,99,7,13,25]) → []
"""



def is_even(num):
    """Return True when num is even, otherwise return False."""
    return num % 2 == 0


def report_evens(numbers):
    """Return the even numbers, preserving their order and duplicates."""
    evens = []
    for num in numbers:
        # Reuse is_even so the filtering rule is defined in one place.
        if is_even(num):
            evens.append(num)
    return evens


if __name__ == "__main__":
    print(report_evens([4, 3, 12, 16, 8, 9, 25]))
    print(report_evens([6, 100, 3, 12, 16, 6, 9, 100]))
    print(report_evens([3, 99, 7, 13, 25]))
    print(is_even(4))
    print(is_even(6))
    print(is_even(3))
