lines = []

with open("input.txt", "r") as f:
    lines = f.readlines()

idx = 50
solution = 0

for line in lines:
    move = line[1:].strip()
    move = int(move)

    if line.startswith("L"):
        idx -= move
    else:
        idx += move

    idx = idx % 100
    
    if idx == 0:
        solution += 1
        
print(f"Solution: {solution}")