# Problem 1: Student and Course classes

# Part (a): Student class
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major

    def get_major(self):
        return self.major

    def set_major(self, major):
        self.major = major

    def __str__(self):
        return f"Student(name={self.name}, major={self.major})"


# Part (b): Course class
class Course:
    def __init__(self, course_name, course_number):
        self.course_name = course_name
        self.course_number = course_number
        self.students = []

    def get_number(self):
        return self.course_number

    def set_number(self, course_number):
        self.course_number = course_number

    def add_student(self, student):
        self.students.append(student)

    def show_student_enrollment(self):
        if not self.students:
            print(f"{self.course_name} {self.course_number} has no students enrolled.")
        else:
            print(f"{self.course_name} {self.course_number} students:")
            for student in self.students:
                print(f" - {student.name} ({student.major})")

    def __str__(self):
        return f"{self.course_name} {self.course_number}"


# Part (c): Demonstration
if __name__ == "__main__":
    student1 = Student("Ava", "Computer Science")
    student2 = Student("Noah", "Biology")

    course = Course("Intro to Programming", 121)
    course.add_student(student1)
    course.add_student(student2)

    print(course)
    course.show_student_enrollment()
    print(student1)
    print(student2)
