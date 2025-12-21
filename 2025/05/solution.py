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

def part1():
    def inRange(id):
        for r in ranges:
            if r[0] <= id <= r[1]:
                return True
        return False

    solution = 0
    for id in ids:
        if inRange(id):
            solution += 1
    return solution


def part2():
    def merge_ranges(rangeA, rangeB) -> list[list]:
        a, b = rangeA
        x, y = rangeB

        if b + 1 >= x and a <= y + 1:
            # Merge into a single range
            return [[min(a, x), max(b, y)]]
        else:
            # No overlap
            return [rangeA, rangeB]

    def merge_all_ranges(all_ranges):
        all_ranges = sorted(all_ranges, key=lambda r: r[0])
        merged = []
        for r in all_ranges:
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

    solution = 0
    for bound in cleaned:
        solution += getRangeLength(bound)
    return solution


if __name__ == "__main__":
    print(f"Solution part 1: {part1()}")
    print(f"Solution part 2: {part2()}")
