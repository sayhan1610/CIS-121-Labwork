# ask the user for an ice cream flavor
print("Available flavors: chocolate, vanilla, strawberry")
flavor = input("Pick a flavor: ")

# check if the flavor is one of the three available options
if flavor == "vanilla" or flavor == "chocolate" or flavor == "strawberry":
    print(f"Here is your {flavor} ice cream!")
else:
    print(f"Sorry, we don't have {flavor} ice cream.")