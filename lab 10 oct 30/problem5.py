# Outcome 11: Define a class with initialized attributes, accessors, and an action.
class Vehicle:
    def __init__(self, make, model, year):
        # Keep the vehicle details on the instance for its methods to use.
        self.make = make
        self.model = model
        self.year = year

    # Each getter reads an attribute; its setter updates that attribute.
    def get_make(self):
        return self.make

    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def print_vehicle_type(self):
        # Match the requested output order: year, make, then model.
        print(f"{self.year} {self.make} {self.model}")


if __name__ == "__main__":
    # Create a vehicle and call its required display method.
    vehicle = Vehicle("Toyota", "Camry", 2021)
    vehicle.print_vehicle_type()
