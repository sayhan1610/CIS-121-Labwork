# Problem 3: Return the course with the smallest grade.

def min_grade(exams):
    """Return the class name with the lowest score."""
    if not exams:
        return None
    return min(exams, key=exams.get)


if __name__ == "__main__":
    print(min_grade({"Physics": 82, "Math": 65, "History": 75, "Biology": 95, "English": 87}))
    print(min_grade({"Chemistry": 78, "Algebra": 88, "History": 72, "Geography": 85}))
    print(min_grade({"Art": 90, "Music": 92, "Drama": 89}))
