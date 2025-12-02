import re

lines = []
numbers = []

pattern = re.compile("^([0-9]+)+$")


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

solution = 0

for line in lines:
    a, b = line.split("-")

    for i in range(int(a), int(b) + 1):

        if has_repetition(i):
            print(f"{a}-{b}: {i} repeat")
            solution += i

print(solution)
