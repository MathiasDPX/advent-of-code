from collections import defaultdict

lines = open("input.txt", "r").read().splitlines()

mymap = defaultdict(list)


def hasCharAt(x, y, map=mymap) -> bool:
    if x < 0 or y < 0 or x > (len(map) - 1) or y > (len(map[0]) - 1):
        # Out of bounds
        return False

    return map[y][x]


for i in range(len(lines)):
    for char in lines[i]:
        mymap[i].append(char == "@")


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


solution = 0
subsolution = None

while subsolution != 0:
    mymap, subsolution = clean_map(mymap)    
    solution += subsolution
    
    print(f"Removed {subsolution} rolls")
    #displayMap(mymap)

print(f"Solution: {solution}")
