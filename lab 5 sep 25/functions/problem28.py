
def pool_time(grade, time):
    time = time.lower()
    table = {
        "k": {"morning": "9 AM", "afternoon": "1 PM"},
        (1, 3): {"morning": "9 AM", "afternoon": "1 PM"},
        (4, 8): {"morning": "10 AM", "afternoon": "2 PM"},
        (9, 12): {"morning": "11 AM", "afternoon": "3 PM"},
    }
    if grade == "k":
        return table["k"][time]
    for grade_range, values in table.items():
        if isinstance(grade_range, tuple) and grade_range[0] <= grade <= grade_range[1]:
            return values[time]
    return "unknown"


if __name__ == "__main__":
    grade = input("Enter grade or 'k': ")
    when = input("Enter Morning or Afternoon: ")
    print(pool_time(grade, when))
