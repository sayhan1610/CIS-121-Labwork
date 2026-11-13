# Problem 9: Employee and Department classes

# Part (a): Employee class
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def __str__(self):
        return f"Employee(name={self.name}, position={self.position})"


# Part (b): Department class
class Department:
    def __init__(self, dept_name, budget):
        self.dept_name = dept_name
        self.budget = budget
        self.employees = []

    def get_budget(self):
        return self.budget

    def set_budget(self, budget):
        self.budget = budget

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_staff_list(self):
        if not self.employees:
            print(f"{self.dept_name} has no employees.")
        else:
            print(f"{self.dept_name} staff:")
            for employee in self.employees:
                print(f" - {employee.name} ({employee.position})")

    def is_large(self):
        return len(self.employees) >= 10

    def __str__(self):
        return f"Department(name={self.dept_name}, budget={self.budget})"


# Part (c): Demonstration
if __name__ == "__main__":
    department = Department("Engineering", 250000)
    employee1 = Employee("Alice", "Developer")
    employee2 = Employee("Ben", "Analyst")

    department.add_employee(employee1)
    department.add_employee(employee2)

    print(department)
    print(employee1)
    print(employee2)
    department.show_staff_list()
    print("Is large?", department.is_large())
