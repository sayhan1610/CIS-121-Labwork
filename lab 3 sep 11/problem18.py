race = input("enter your race: ").lower()
character_class = input("enter your class: ").lower()

# Store health points for each valid race and character class combination.
health_points = {
    "elf": {"warrior": 150, "bard": 75, "wizard": 25},
    "ogre": {"warrior": 200, "bard": 100, "wizard": 50},
}

# Validate both selections before looking up the health points.
if race in health_points and character_class in health_points[race]:
    health_points_value = health_points[race][character_class]
    print(f"your health points are {health_points_value}.")
else:
    print("invalid race or class.")