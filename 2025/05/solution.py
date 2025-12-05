ranges = []
ids = []

data = open("input.txt", "r").read().splitlines()

splitted = False
for line in data:
    if len(line) == 0:
        splitted = True
        continue

    if not splitted:
        ranges.append([int(x) for x in line.split("-")])
    else:
        ids.append(int(line))


def inRange(id):
    for range in ranges:
        if range[0] <= id <= range[1]:
            return True

    return False


solution1 = 0
for id in ids:
    if inRange(id):
        solution1 += 1

print(f"Solution part 1: {solution1}")


def merge_ranges(rangeA, rangeB) -> list[list]:
    a, b = rangeA
    x, y = rangeB

    # Check if ranges overlap or are adjacent
    if b + 1 >= x and a <= y + 1:
        # Merge into a single range
        return [[min(a, x), max(b, y)]]
    else:
        # No overlap
        return [rangeA, rangeB]


# Merge all ranges until no more merges are possible
def merge_all_ranges(ranges):
    ranges = sorted(ranges, key=lambda r: r[0])
    merged = []
    for r in ranges:
        if not merged:
            merged.append(r)
        else:
            last = merged[-1]
            merged_ranges = merge_ranges(last, r)
            if len(merged_ranges) == 1:
                merged[-1] = merged_ranges[0]
            else:
                merged.append(r)
    return merged


def getRangeLength(bounds):
    return abs(bounds[0] - bounds[1]) + 1


cleaned = merge_all_ranges(ranges)

solution2 = 0
for bound in cleaned:
    solution2 += getRangeLength(bound)

print(f"Solution part 2: {solution2}")
