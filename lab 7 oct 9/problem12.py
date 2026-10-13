# Problem 12: Return the total donations from a dictionary of donor amounts.

def total_donations(donations):
    """Return the sum of all values in the donations dictionary."""
    return sum(donations.values())


if __name__ == "__main__":
    print(total_donations({"John": 100, "Sarah": 200, "Mike": 50}))
    print(total_donations({"Anna": 500, "Tom": 1000, "Jerry": 1500}))
    print(total_donations({"Chris": 25, "Alex": 30, "Morgan": 45}))
