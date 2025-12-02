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


with open("input.txt", "r") as f:
    lines = f.read().split(",")

solution = 0

for line in lines:
    a, b = line.split("-")

    for i in range(int(a), int(b) + 1):

        if has_repetition(i):
            solution += i

print(solution)
