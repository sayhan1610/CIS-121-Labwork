total_knuts = int(input("Enter the number of knuts: "))

# Define the conversion rates between the wizarding currencies.
knuts_per_sickle = 29
sickles_per_galleon = 17
knuts_per_galleon = knuts_per_sickle * sickles_per_galleon

# Convert the total into galleons, then convert the remainder into smaller units.
galleons = total_knuts // knuts_per_galleon
remainder = total_knuts % knuts_per_galleon

sickles = remainder // knuts_per_sickle
knuts = remainder % knuts_per_sickle

# Build a readable result while using singular or plural unit names.
result = []

if galleons > 0:
    result.append(f"{galleons} galleon" if galleons == 1 else f"{galleons} galleons")

if sickles > 0:
    result.append(f"{sickles} sickle" if sickles == 1 else f"{sickles} sickles")

if knuts > 0:
    result.append(f"{knuts} knut" if knuts == 1 else f"{knuts} knuts")

print(" ".join(result))