lines = []

lines = open('input.txt', 'r').read().splitlines(False)

digits = 12 # 2 for first part
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
        
    top = int(''.join(selected))
    result += top
    
print("Solution:", result)
