grade = input("enter your grade: ").lower()
time_of_day = input("enter morning or afternoon: ").lower()

# Convert the entered grade into one of the available grade groups.
if grade == "k" or grade == "kindergarten" or grade == "0":
    grade_group = "k, 1-3"
else:
    grade_number = int(grade)
    if 1 <= grade_number <= 3:
        grade_group = "k, 1-3"
    elif 4 <= grade_number <= 8:
        grade_group = "4-8"
    elif 9 <= grade_number <= 12:
        grade_group = "9-12"
    else:
        print("grade is outside the allowed range.")
        raise SystemExit

pool_times = {
    "k, 1-3": {"morning": "9 am", "afternoon": "1 pm"},
    "4-8": {"morning": "10 am", "afternoon": "2 pm"},
    "9-12": {"morning": "11 am", "afternoon": "3 pm"},
}

# Validate the requested time and display the matching pool opening.
if time_of_day not in pool_times[grade_group]:
    print("invalid time option.")
else:
    print(f"the pool is open at {pool_times[grade_group][time_of_day]}.")