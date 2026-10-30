# Outcome 11: Define a class with an initialized temperature, accessors, and a conversion.
class TemperatureInCelsius:
    def __init__(self, temp_value):
        # Store the temperature in Celsius as required by the assignment.
        self.temp_value = temp_value

    # The getter reads the Celsius value; the setter updates it.
    def get_temp_value(self):
        return self.temp_value

    def set_temp_value(self, temp_value):
        self.temp_value = temp_value

    def to_fahrenheit(self):
        # Convert Celsius to Fahrenheit using the specified formula.
        return self.temp_value * 9 / 5 + 32


if __name__ == "__main__":
    # Create a temperature and demonstrate its conversion.
    temperature = TemperatureInCelsius(25)
    print(temperature.to_fahrenheit())
