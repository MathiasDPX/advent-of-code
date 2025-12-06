from collections import defaultdict
import math

data = open("input.txt", "r").read().splitlines()

operations = defaultdict(list)

for i in range(len(data)):
    numbers = data[i].strip().split(" ")
    numbers = [number for number in numbers if len(number) != 0]
    
    for j in range(len(numbers)):
        operations[j].append(numbers[j])


solution = 0
for i, operation in operations.items():
    operator = operation[-1]
    operants = operation[:-1]
    operants = [int(i) for i in operants]
    
    if operator == "*":
        solution += math.prod(operants)
    elif operator == "+":
        solution += sum(operants)
    
print(f"Solution: {solution}")