# get light color from the user as input
print("Pick between green, yellow or red! (case sensitive)")
light_color = input("Enter the light color: ")

# check color for actions to perform
if light_color == "green":
    print("go")
elif light_color == "yellow":
    print("yield")
elif light_color == "red":
    print("stop")
else:
    print("invalid color")