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

class Star:
    def __init__(self, name):
        self.name = name
        
    #getters
    def get_name(self):
        return self.name + " is a star"
    #setters
    def set_name(self, new_name):
        self.name = new_name
        
class PlanetarySystem:
    def __init__(self, a_star):
        self.star = a_star
        self.planet_list = []
        
    def add_planet(self, new_planet):
        self.planet_list.append(new_planet) # this method adds a new planet to the list of planets

    def show_planets(self):
        print(f"Planets orbiting {self.star.get_name()}:")
        for planet in self.planet_list:
            print(f" - {planet.get_name()}")

sun = Star("Sun")
solar_system = PlanetarySystem(sun)

mercury = Planet("Mercury", 2439.7, 3.3011e23, 57.91e6)
solar_system.add_planet(mercury)

venus = Planet("Venus", 6051.8, 4.8675e24, 108.2e6)
solar_system.add_planet(venus)

earth = Planet("Earth", 6371, 5.97237e24, 149.6e6)
solar_system.add_planet(earth)


solar_system.show_planets()


