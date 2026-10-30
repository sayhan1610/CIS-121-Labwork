import math
class Planet:
    def __init__(self, a_name, a_radius, a_mass, a_distance):
        self.name = a_name
        self.radius = a_radius
        self.mass = a_mass
        self.dist = a_distance
        pass
    
    # add getters
    def get_name(self):
        return self.name
    def get_mass(self):
        return self.mass
    def get_radius(self):
        return self.radius
    def get_volume(self):
        volume = 4/3 * math.pi * self.get_radius()**3
        return volume
    
    # setters
    def set_name(self, new_name):
        self.name = new_name
    
    
planet1 = Planet("x23", 12, 345, 8374)
planet2 = Planet("z46", 76, 324, 3123)

#here...
#print planet1's name
print(planet1.get_name())
#change planet1's name
print(planet1.set_name("p41"))
#print planet1's name so we can see the change 
print(planet1.get_name())
