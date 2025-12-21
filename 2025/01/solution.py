lines = []

with open("input.txt", "r") as f:
    lines = f.readlines()


def part1():
    idx = 50
    solution = 0

    for line in lines:
        move = line[1:].strip()
        move = int(move)

        if line.startswith("L"):
            move *= -1

        idx += move
        idx %= 100

        if idx == 0:
            solution += 1

    return solution


def part2():
    idx = 50
    solution = 0

    for line in lines:
        move = line[1:].strip()
        move = int(move)

        step = 1
        if line.startswith("L"):
            step = -1

        while move != 0:
            idx += step
            move -= 1

            idx = idx % 100

            if idx == 0:
                solution += 1

    return solution


if __name__ == "__main__":
    print(f"Solution part 1: {part1()}")
    print(f"Solution part 2: {part2()}")
