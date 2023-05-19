import hashlib

def part1(file):
    with open(file, "r") as file:
        key = file.read()
        trial = 0
        data = key + str(trial)
        result = hashlib.md5(data.encode()).hexdigest()
        while result[:5] != "00000":
            trial += 1
            data = key + str(trial)
            result = hashlib.md5(data.encode()).hexdigest()
        return(trial)
#print(part1("input.txt"))

def part2(file):
    with open(file, "r") as file:
        key = file.read()
        trial = 0
        data = key + str(trial)
        result = hashlib.md5(data.encode()).hexdigest()
        while result[:6] != "000000":
            trial += 1
            data = key + str(trial)
            result = hashlib.md5(data.encode()).hexdigest()
        return(trial)
print(part2("input.txt"))
