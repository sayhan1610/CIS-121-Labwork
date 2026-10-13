# Problem 18: Return employees whose salary is above a given threshold.

def high_earners(employee_salaries, salary):
    """Return the names of employees earning more than salary."""
    names = []
    for employee, pay in employee_salaries.items():
        if pay > salary:
            names.append(employee)
    return names


if __name__ == "__main__":
    print(high_earners({"Alice": 50000, "Bob": 75000, "Charlie": 100000}, 60000))
    print(high_earners({"David": 30000, "Emma": 45000, "Frank": 50000}, 40000))
    print(high_earners({"George": 25000, "Hannah": 27000, "Ian": 29000}, 30000))
