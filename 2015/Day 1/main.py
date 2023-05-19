def part1(file):
    level = 0
    with open(file, "r") as file:
        content = file.read()
        for character in content:
            if character == "(":
                level = level + 1
            else:
                level = level - 1
    return level
print(part1("input.txt"))

def part2(file):
    level = 0
    position = 0
    with open(file, "r") as file:
        content = file.read()
        for character in content:
            position = position + 1
            if character == "(":
                level = level + 1
            else:
                level = level - 1
                if level < 0:
                    break
    return position
print(part2("input.txt"))
