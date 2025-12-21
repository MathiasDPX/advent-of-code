lines = []

lines = open("input.txt", "r").read().splitlines(False)


def solve(digits):
    result = 0

    for line in lines:
        length = len(line)
        selected = []
        start = 0

        for i in range(digits):
            end = length - (digits - 1 - i)
            best_idx = start

            for j in range(start, end):
                if line[j] > line[best_idx]:
                    best_idx = j

            selected.append(line[best_idx])
            start = best_idx + 1

        top = int("".join(selected))
        result += top

    return result


def part1():
    return solve(2)


def part2():
    return solve(12)


if __name__ == "__main__":
    print(f"Solution part 1: {part1()}")
    print(f"Solution part 2: {part2()}")
