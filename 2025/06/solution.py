from collections import defaultdict
from math import prod

data = open("input.txt", "r").read().splitlines()


def part1():
    solution = 0

    operations = defaultdict(list)

    for i in range(len(data)):
        numbers = data[i].strip().split(" ")
        numbers = [number for number in numbers if len(number) != 0]

        for j in range(len(numbers)):
            operations[j].append(numbers[j])

    for i, operation in operations.items():
        operator = operation[-1]
        operants = operation[:-1]
        operants = [int(i) for i in operants]

        if operator == "*":
            solution += prod(operants)
        elif operator == "+":
            solution += sum(operants)

    return solution


def part2():
    solution = 0
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

    rotated_data.append(buffer)  # add last row

    operators = data[-1].split(" ")
    operators = [operator.strip() for operator in operators if operator != ""]

    for i in range(len(operators)):
        operator = operators[i]
        if operator == "+":
            solution += sum(rotated_data[i])
        else:
            solution += prod(rotated_data[i])
            
    return solution


if __name__ == "__main__":
    print(f"Solution part 1: {part1()}")
    print(f"Solution part 2: {part2()}")