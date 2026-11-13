# Lab 12 Problem 3: ComplexNumber class
# Rubric focus: __eq__ compares complex numbers and __str__ prints
# the real and imaginary parts clearly.


class ComplexNumber:
    def __init__(self, a, b):
        # Store the real part (a) and imaginary part (b).
        self.a = a
        self.b = b

    def __eq__(self, other):
        # A complex number is equal only when both parts match.
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        return self.a == other.a and self.b == other.b

    def __str__(self):
        # Print in the standard form "a + bi" or "a - bi".
        if self.b == 0:
            return str(self.a)

        sign = "+" if self.b > 0 else "-"
        return f"{self.a} {sign} {abs(self.b)}i"


if __name__ == "__main__":
    z1 = ComplexNumber(3, 2)
    z2 = ComplexNumber(-1, 4)
    z3 = ComplexNumber(3, 2)

    # Compare complex numbers using custom equality.
    print("z1 == z2:", z1 == z2)
    print("z1 == z3:", z1 == z3)

    print("z1:", z1)
    print("z2:", z2)
    print("z3:", z3)
