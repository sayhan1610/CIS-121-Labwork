
def is_boiling(temp):
    unit = temp[-1].upper()
    temperature = float(temp[:-1])

    if unit == "F":
        return temperature >= 212
    if unit == "C":
        return temperature >= 100
    raise ValueError("Temperature must end with 'F' or 'C'.")


if __name__ == "__main__":
    test = input("Enter a temperature like 212F or 100C: ")
    print(is_boiling(test))
