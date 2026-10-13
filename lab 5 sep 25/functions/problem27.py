
def resting_rate(age, athl_goal):
    athl_goal = athl_goal.lower()
    table = {
        (20, 39): {"above average": "47-72", "below average": "73-93"},
        (40, 59): {"above average": "46-71", "below average": "72-94"},
        (60, 79): {"above average": "45-70", "below average": "71-97"},
    }
    for age_range, values in table.items():
        if age_range[0] <= age <= age_range[1]:
            return values.get(athl_goal, "unknown")
    return "unknown"


if __name__ == "__main__":
    age = int(input("Enter age: "))
    goal = input("Enter athletic goal: ")
    print(resting_rate(age, goal))
