data = open("input.txt", "r").read().splitlines()

connections = {}

for line in data:
    in_rack, out_racks = line.split(": ")
    out_racks = out_racks.split(" ")
    connections[in_rack] = out_racks


def part1(start="you", end="out"):
    childrens = connections[start]

    outs = 0
    for children in childrens:
        if children == end:
            outs += 1
            continue

        outs += part1(children)

    return outs


print(f"Solution part 1: {part1()}")