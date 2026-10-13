
def design_run(width, length, pattern):
    rows = []
    for _ in range(length):
        rows.append(pattern * width)
    return '\n'.join(rows)


if __name__ == "__main__":
    w = int(input("Enter width: "))
    l = int(input("Enter length: "))
    pattern = input("Enter a pattern character: ")
    print(design_run(w, l, pattern))
