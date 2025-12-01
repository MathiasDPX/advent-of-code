lines = []

with open("input.txt", "r") as f:
    lines = f.readlines()

idx = 50

solution1 = 0
solution2 = 0

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
            solution2 += 1
    
    if idx == 0:
            solution1 += 1

print(f"Solution part 1: {solution1}")
print(f"Solution part 2: {solution2}")