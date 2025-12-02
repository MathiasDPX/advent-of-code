lines = []

def has_repetition(s) -> bool:
    s = str(s)
    i = (s+s).find(s, 1, -1)
    
    if i >= 1:
        return True

    return False


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
