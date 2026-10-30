# Outcome 11: Define a class with initialized attributes, accessors, and actions.
class Student:
    def __init__(self, name, major, gpa):
        # Store the student's details for the introduction and study method.
        self.name = name
        self.major = major
        self.gpa = gpa

    # Each getter reads an attribute; its setter updates that attribute.
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_major(self):
        return self.major

    def set_major(self, major):
        self.major = major

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        self.gpa = gpa

    def introduce(self):
        print(f"Hi, I'm {self.name}. I'm studying {self.major}.")

    def study_for_exam(self):
        old_gpa = self.gpa
        # Add 0.2 points, round to one decimal place, and cap the GPA at 4.0.
        self.gpa = min(4.0, round(self.gpa + 0.2, 1))
        print(
            f"I'm hitting the books! My GPA increased from "
            f"{old_gpa:.1f} to {self.gpa:.1f}."
        )


if __name__ == "__main__":
    # Create a student and demonstrate both required actions.
    student = Student("Maria", "Computer Science", 3.5)
    student.introduce()
    student.study_for_exam()
