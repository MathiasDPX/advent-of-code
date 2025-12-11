from functools import lru_cache

data = open("input.txt", "r").read().splitlines()

connections = {}

for line in data:
    in_rack, out_racks = line.split(": ")
    out_racks = out_racks.split(" ")
    connections[in_rack] = out_racks


@lru_cache(maxsize=None)
def part1(start=None, end=None):
    start = start or "you"
    end = end or "out"

    if start == end:
        return 0  # no move counts when already at end

    childrens = connections.get(start, ())
    if not childrens:
        return 0

    outs = 0

    for child in childrens:
        if child == end:
            outs += 1
        else:
            outs += part1(child, end)

    return outs


def part2():
    first = part1("svr", "fft")
    second = part1("fft", "dac")
    third = part1("dac", "out")
    return first * second * third


print(f"Solution part 1: {part1()}")
print(f"Solution part 2: {part2()}")
