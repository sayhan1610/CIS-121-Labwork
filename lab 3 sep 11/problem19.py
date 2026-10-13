"""grade = input("enter your grade: ").lower()
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
    print(f"the pool is open at {pool_times[grade_group][time_of_day]}.")"""
    
# Take inputs from user
age = int(input ("Enter your age : "))
goal = input("Enter athletism goal (below/above): ")
# determine goal of the user
if goal == "above":
    if age >= 20 and age <= 39:
        print ("Resting heart rate should be 47-72")
    elif age >= 40 and age <= 59:
        print ("Resting heart rate should be 46-71")
    elif age >= 60 and age <= 79:
        print ("Resting heart rate should be 45-70")
    else:
        print ("Unsupported age")

elif goal == "below":
    if age >= 20 and age <= 39:
        print ("Resting heart rate should be 73-93")
    elif age >= 40 and age <= 59:
        print ("Resting heart rate should be 72-94")
    elif age >= 60 and age <= 79:
        print ("Resting heart rate should be 71-97")
    else:
        print ("Unsupported age")

else:
    print ("Invalid goal , Pick between above or below")