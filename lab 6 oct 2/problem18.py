# Problem 18: Count the number of lag days in a list of mileage totals.

def lag_days(miles):
    """Return how many times the next mileage is smaller than the previous one."""
    count = 0
    for index in range(1, len(miles)):
        if miles[index] < miles[index - 1]:
            count += 1
    return count


if __name__ == "__main__":
    print(lag_days([5, 3, 2, 1]))
    print(lag_days([10, 11, 12, 9, 10]))
    print(lag_days([6, 5, 4, 3, 2, 9]))
    print(lag_days([9, 9]))
