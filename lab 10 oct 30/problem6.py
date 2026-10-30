# Outcome 11: Define a class with initialized attributes, accessors, and an action.
class Course:
    def __init__(self, course_code, course_name, instructor):
        # Store the course details so the accessors and print_info can use them.
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor

    # Each getter reads an attribute; its setter updates that attribute.
    def get_course_code(self):
        return self.course_code

    def set_course_code(self, course_code):
        self.course_code = course_code

    def get_course_name(self):
        return self.course_name

    def set_course_name(self, course_name):
        self.course_name = course_name

    def get_instructor(self):
        return self.instructor

    def set_instructor(self, instructor):
        self.instructor = instructor

    def print_info(self):
        # Format the course details as specified in the assignment.
        print(
            f"{self.course_code}: {self.course_name} "
            f"taught by {self.instructor}"
        )


if __name__ == "__main__":
    # Create a course and call its required display method.
    course = Course(
        "CIS101", "Introduction to programming", "Matt"
    )
    course.print_info()
