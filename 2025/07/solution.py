from copy import deepcopy

data = open("input.txt", "r").read().splitlines()

for i in range(len(data)):
    data[i] = list(data[i])


def compute_classical(data):
    data = deepcopy(data)
    splitcount = 0
    map = data
    for i in range(len(map)):
        for j in range(len(map[i])):
            char = map[i][j]

            if i == 0:
                if char == "S":
                    map[i][j] = "|"

                continue

            parent = map[i - 1][j]

            if char == "|":
                continue
            elif char == "^" and parent == "|":
                splitcount += 1
                map[i][j + 1] = "|"
                map[i][j - 1] = "|"
            elif parent == "|":
                map[i][j] = "|"

    return splitcount


def compute_quantum(data):
    data = deepcopy(data)
    map = data
    
    def compute_split(x, y):
        if type(map[y][x]) == str:
            map[y][x] = parent
        else:
            map[y][x] += parent
        
        return map[y][x]
    
    for i in range(len(map)):
        for j in range(len(map[i])):
            char = map[i][j]

            if i == 0:
                if char == "S":
                    map[i][j] = 1

                continue

            parent = map[i - 1][j]

            if char == "^" and type(parent) == int:
                compute_split(j-1, i)
                compute_split(j+1, i)
            elif type(parent) == int:
                compute_split(j, i)

    timelines = 0
    for char in map[-1]:
        if type(char) == int:
            timelines += char

    return timelines


print(f"Solution part 1: {compute_classical(data)}")
print(f"Solution part 2: {compute_quantum(data)}")
