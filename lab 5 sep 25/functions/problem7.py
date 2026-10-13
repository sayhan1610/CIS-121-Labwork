
def highway_directions(highway_num):
    if highway_num < 1 or highway_num > 999:
        return f"I-{highway_num} is an invalid highway number"

    if 100 <= highway_num <= 999:
        if highway_num % 100 == 0:
            return f"I-{highway_num} is an invalid highway number"
        primary = highway_num % 100
        if primary % 2 == 0:
            return f"I-{highway_num} services I-{primary} east/west"
        return f"I-{highway_num} services I-{primary} north/south"

    if highway_num % 2 == 0:
        return f"I-{highway_num} runs east/west"
    return f"I-{highway_num} runs north/south"


if __name__ == "__main__":
    num = int(input("Enter a highway number: "))
    print(highway_directions(num))
