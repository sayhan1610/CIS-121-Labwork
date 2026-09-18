highway = int(input("pick a highway number: "))

# Validate the highway number and determine its direction from parity.
if highway < 1 or highway > 999:
    print("invalid highway number")
elif highway <= 99:
    if highway % 2 == 0:
        print(f"highway {highway} runs east/west")
    else:
        print(f"highway {highway} runs north/south")
elif highway % 100 == 0:
    print("invalid highway number")
elif highway % 2 == 0:
    print(f"highway {highway} runs east/west")
else:
    print(f"highway {highway} runs north/south")