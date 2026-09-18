# ask Luke to input a name
name = input("Enter a name: ")

# check the name and output the corresponding relation
if name == "Darth Vader":
    print("Father")
elif name == "Leia":
    print("Sister")
elif name == "Han":
    print("Brother in law")
elif name == "R2D2":
    print("Droid")
else:
    print("unknown")