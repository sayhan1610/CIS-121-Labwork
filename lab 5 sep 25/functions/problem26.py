
def battery_counter(e_dolls, rc_cars, robo_dogs):
    return e_dolls * 2 + rc_cars * 4 + robo_dogs * 6


if __name__ == "__main__":
    dolls = int(input("Enter electronic dolls: "))
    cars = int(input("Enter remote-controlled cars: "))
    dogs = int(input("Enter robot dogs: "))
    print(battery_counter(dolls, cars, dogs))
