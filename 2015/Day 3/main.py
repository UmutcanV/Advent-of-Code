def part1(file):
    houses = dict()
    x = 0
    y = 0
    houses[(x, y)] = 1
    with open(file, "r") as file:
        content = file.read()
        for character in content:
            if character == "^":
                y += 1
            elif character == "v":
                y -= 1
            elif character == "<":
                x -= 1
            elif character == ">":
                x += 1
            houses[(x,y)] = 1
    return(len(houses))
#print(part1("input.txt"))

def part2(file):
    houses= dict()
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    houses[(x1, y1)] = 2
    with open(file, "r") as file:
        content = file.read()
        for index,character in enumerate(content):
            if index % 2 == 1:
                if character == "^":
                    y2 += 1
                elif character == "v":
                    y2 -= 1
                elif character == "<":
                    x2 -= 1
                elif character == ">":
                    x2 += 1
                houses[(x2, y2)] = 1
            else:
                if character == "^":
                    y1 += 1
                elif character == "v":
                    y1 -= 1
                elif character == "<":
                    x1 -= 1
                elif character == ">":
                    x1 += 1
                houses[(x1, y1)] = 1
    return(len(houses))
print(part2("input.txt"))