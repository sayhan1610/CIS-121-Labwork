'''The normal human body temperature is 98.6F in Fahrenheit and 37C in Celsius. Create a function
that determines if the temp is considered a fever (above normal body temperature) or not. temp will
be measured in Fahrenheit or Celsius.
Notice: The F or C will always be the last character in the string.
Examples:

· is_fever("99F") -> True,
· is_fever("37C") -> False,
· is_fever("98F") -> False,'''


def is_fever(temp):
    unit = temp[-1].upper()
    temperature = float(temp[:-1])

    if unit == "F":
        return temperature > 98.6
    if unit == "C":
        return temperature > 37

    raise ValueError("Temperature must end with 'F' or 'C'.")


if __name__ == "__main__":
    value = input("Enter a temperature like 99F or 37C: ")
    print(is_fever(value))