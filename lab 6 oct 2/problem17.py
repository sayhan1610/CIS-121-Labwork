# Problem 17: Count the number of progress days in a list of mileage totals.

def progress_days(miles):
    """Return how many times the next mileage is greater than the previous one."""
    count = 0
    for index in range(1, len(miles)):
        if miles[index] > miles[index - 1]:
            count += 1
    return count


if __name__ == "__main__":
    print(progress_days([3, 4, 1, 2]))
    print(progress_days([10, 11, 12, 9, 10]))
    print(progress_days([6, 5, 4, 3, 2, 9]))
    print(progress_days([9, 9]))
