from collections import defaultdict
from copy import deepcopy

lines = open("input.txt", "r").read().splitlines()
mymap = defaultdict(list)


for i in range(len(lines)):
    for char in lines[i]:
        mymap[i].append(char == "@")


def hasCharAt(x, y, map=mymap) -> bool:
    if x < 0 or y < 0 or x > (len(map) - 1) or y > (len(map[0]) - 1):
        # Out of bounds
        return False

    return map[y][x]


def getNeighbors(x, y, map=mymap):
    neighbors = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if hasCharAt(i, j, map=map):
                neighbors += 1

    return neighbors


def clean_map(map):
    cleaned_map = defaultdict(list)
    subsolution = 0

    for y in range(len(map)):
        for x in range(len(map[i])):
            cell = map[y][x]
            if not cell:
                cleaned_map[y].append(False)
                # no cell here
                continue

            neighbors = getNeighbors(x, y, map=map)

            if neighbors > 4:
                cleaned_map[y].append(True)
            else:
                cleaned_map[y].append(False)
                subsolution += 1

    return cleaned_map, subsolution


def displayMap(map):
    for y in range(len(map)):
        for x in range(len(map[i])):
            print("@" if map[y][x] else ".", end="")

        print("")


def part1():
    map = deepcopy(mymap)
    _, solution = clean_map(map)

    return solution


def part2():
    map = deepcopy(mymap)
    solution = 0
    subsolution = None

    while subsolution != 0:
        map, subsolution = clean_map(map)
        solution += subsolution

    return solution


if __name__ == "__main__":
    print(f"Solution part 1: {part1()}")
    print(f"Solution part 2: {part2()}")
