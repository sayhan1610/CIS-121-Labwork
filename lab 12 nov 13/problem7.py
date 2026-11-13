# Lab 12 Problem 7: RationalNumber class
# Rubric focus: __add__ adds fractions using a common denominator
# and __str__ prints the result as a fraction.


class RationalNumber:
    def __init__(self, numerator, denominator):
        # Save the fraction as numerator/denominator.
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        # Add fractions by finding a common denominator.
        if not isinstance(other, RationalNumber):
            return NotImplemented

        common_denominator = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        return RationalNumber(new_numerator, common_denominator)

    def __str__(self):
        # Print the fraction in a nice format.
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    r1 = RationalNumber(1, 3)
    r2 = RationalNumber(1, 2)

    result = r1 + r2

    print("r1:", r1)
    print("r2:", r2)
    print("r1 + r2:", result)
