lines = []


def has_repetition(s) -> bool:
    s = str(s)
    n = len(s)

    if n % 2 != 0:
        return False

    half = n // 2
    left = s[:half]
    right = s[half:]

    return left == right


def is_periodic(s) -> bool:
    s = str(s)
    i = (s + s).find(s, 1, -1)

    if i >= 1:
        return True

    return False

def has_repetition(s) -> bool:
    s = str(s)
    n = len(s)

    if n % 2 != 0:
        return False

    half = n // 2
    left = s[:half]
    right = s[half:]

    return left == right

with open("input.txt", "r") as f:
    lines = f.read().split(",")

def get_password(func):
    solution = 0
    for line in lines:
        a, b = line.split("-")

        for i in range(int(a), int(b) + 1):
            if func(i):
                solution += i
    
    return solution

def part1():
    return get_password(has_repetition)

def part2():
    return get_password(is_periodic)

if __name__ == "__main__":
    print(f"Solution part 1: {part1()}")
    print(f"Solution part 2: {part2()}")