
def traffic_light(color):
    color = color.lower()
    if color == "red":
        return "Stop"
    if color == "green":
        return "Go"
    if color == "yellow":
        return "Yield"
    raise ValueError("Unknown traffic light color.")


if __name__ == "__main__":
    light = input("Enter the traffic light color: ")
    print(traffic_light(light))
