age = int(input("enter your age: "))
goal = input("enter your athleticism goal: ").lower()

# Place the user into the matching age group.
if 20 <= age <= 39:
    age_group = "20-39"
elif 40 <= age <= 59:
    age_group = "40-59"
elif 60 <= age <= 79:
    age_group = "60-79"
else:
    print("age is outside the range for this table.")
    raise SystemExit

heart_rate_ranges = {
    "20-39": {
        "above average": "47-72",
        "average": "50-76",
        "below average": "73-93",
    },
    "40-59": {
        "above average": "46-71",
        "average": "49-75",
        "below average": "72-94",
    },
    "60-79": {
        "above average": "45-70",
        "average": "48-74",
        "below average": "71-97",
    },
}

# Look up and display the target heart-rate range for the goal.
if goal not in heart_rate_ranges[age_group]:
    print("invalid athleticism goal.")
else:
    target_range = heart_rate_ranges[age_group][goal]
    print(f"your resting heart rate should be between {target_range}.")