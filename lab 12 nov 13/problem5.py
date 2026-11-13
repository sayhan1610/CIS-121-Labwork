# Lab 12 Problem 5: Time class
# Rubric focus: __add__ carries over minutes into hours and __str__
# prints the result in an easy-to-read format.


class Time:
    def __init__(self, hours, minutes):
        # Store the time as hours and minutes.
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        # Convert both times to total minutes, add them, then carry
        # leftover minutes into hours so the format stays valid.
        if not isinstance(other, Time):
            return NotImplemented

        total_minutes = (self.hours * 60 + self.minutes) + (other.hours * 60 + other.minutes)
        new_hours, new_minutes = divmod(total_minutes, 60)
        return Time(new_hours, new_minutes)

    def __str__(self):
        # Print the time in a readable hour/minute format.
        return f"{self.hours}h {self.minutes}m"


if __name__ == "__main__":
    t1 = Time(1, 30)
    t2 = Time(2, 45)

    result = t1 + t2

    print("t1:", t1)
    print("t2:", t2)
    print("t1 + t2:", result)
