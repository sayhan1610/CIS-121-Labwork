# Outcome 11: Define a class with initialized attributes, accessors, and actions.
class Employee:
    def __init__(self, name, title, salary):
        # Save the employee details for the greeting and raise request.
        self.name = name
        self.title = title
        self.salary = salary

    # Each getter reads an attribute; its setter updates that attribute.
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def greeting(self):
        print(f"Hello. My name is {self.name}. I'm the {self.title}.")

    def request_raise(self):
        # A requested 6% raise is the current salary multiplied by 1.06.
        new_salary = self.salary * 1.06
        print(
            f"I'm currently making ${self.salary:g}. "
            f"I'd like new salary of ${new_salary:g}."
        )


if __name__ == "__main__":
    # Create an employee and demonstrate both required actions.
    employee = Employee("Eugene", "CEO", 100)
    employee.greeting()
    employee.request_raise()
