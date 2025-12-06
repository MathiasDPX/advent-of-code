from math import prod

data = open("input.txt", "r").read().splitlines()
rotated_data = []

buffer = []
for i in range(len(data[-1])):
    number = ""
    for j in range(len(data[:-1])):
        number += data[j][i]
        
    number = number.strip()
    
    if len(number) == 0:
        rotated_data.append(buffer)
        buffer = []
    else:
        buffer.append(int(number))
        
rotated_data.append(buffer) # add last row

operators = data[-1].split(" ")
operators = [operator.strip() for operator in operators if operator != ""]

solution = 0
for i in range(len(operators)):
    operator = operators[i]
    if operator == "+":
        solution += sum(rotated_data[i])
    else:
        solution += prod(rotated_data[i])
        
print(f"Solution part 2: {solution}")