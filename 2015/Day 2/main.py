def part1(file):
    sum = 0
    with open(file, "r") as file:
        content = file.readlines()
        for lines in content:
            numbers = [int (num) for num in lines.strip().split("x")]
            numbers.sort()

            l = numbers[0]
            w = numbers[1]
            h = numbers[2]

            p1 = 3 * l * w
            p2 = 2 * w * h
            p3 = 2 * h * l

            sum += p1 + p2 + p3
    return(sum)
print(part1("input.txt"))

def part2(file):
    sum = 0
    with open(file, "r") as file:
        content = file.readlines()
        for lines in content:
            numbers = [int (num) for num in lines.strip().split("x")]
            numbers.sort()

            l = numbers[0]
            w = numbers[1]
            h = numbers[2]

            p1 =  2 * l + 2 * w
            p2 = l * w * h

            sum += p1 + p2
    return(sum)
print(part2("input.txt"))
