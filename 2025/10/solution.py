# thx https://blog.geographer.fr/z3-intro

from z3 import *
import re

BUTTONS_PATTERN = r"\(([^)]*)\)"

data = open("input.txt", "r").read().splitlines()


class LightMachine:
    def __init__(self, line):
        self.target_lights = [1 if char == "#" else 0 for char in line.split("]")[0][1:]]
        size = len(self.target_lights)

        self.buttons = []
        for match in re.finditer(BUTTONS_PATTERN, line):
            keys_str = match.group(1)
            keys = [int(key) for key in keys_str.split(",")]
            matrix = [1 if i in keys else 0 for i in range(size)]
            self.buttons.append(matrix)


class JoltageMachine:
    def __init__(self, line):
        self.target_joltage = [int(char) for char in line.split("{")[-1][:-1].split(",")]
        size = len(self.target_joltage)

        self.buttons = []
        for match in re.finditer(BUTTONS_PATTERN, line):
            keys_str = match.group(1)
            keys = [int(key) for key in keys_str.split(",")]
            matrix = [1 if i in keys else 0 for i in range(size)]
            self.buttons.append(matrix)


lightmachines: list[LightMachine] = []
joltagemachines: list[JoltageMachine] = []
for line in data:
    lightmachines.append(LightMachine(line))
    joltagemachines.append(JoltageMachine(line))


def part1():
    solution = 0
    for machine in lightmachines:
        optimizer = Optimize()
        button_vars = [Int(f"button_{i}") for i in range(len(machine.buttons))]

        for var in button_vars:
            optimizer.add(var >= 0)

        for position in range(len(machine.target_lights)):
            effect_sum = Sum(
                [
                    button_vars[i] * machine.buttons[i][position]
                    for i in range(len(machine.buttons))
                ]
            )
            optimizer.add(effect_sum % 2 == machine.target_lights[position])

        # minimize total presses
        total_presses = Sum(button_vars)
        optimizer.minimize(total_presses)

        if optimizer.check() == sat:
            model = optimizer.model()
            min_presses = sum(model[var].as_long() for var in button_vars)
            solution += min_presses

    return solution


def part2():
    solution = 0
    for machine in joltagemachines:
        optimizer = Optimize()

        button_vars = [Int(f"button_{i}") for i in range(len(machine.buttons))]

        # all press counts must be non-negative
        for var in button_vars:
            optimizer.add(var >= 0)

        # sum of button effects equals target joltage
        for position in range(len(machine.target_joltage)):
            effect_sum = Sum(
                [
                    button_vars[i] * machine.buttons[i][position]
                    for i in range(len(machine.buttons))
                ]
            )
            optimizer.add(effect_sum == machine.target_joltage[position])

        # minimize total presses
        total_presses = Sum(button_vars)
        optimizer.minimize(total_presses)

        if optimizer.check() == sat:
            model = optimizer.model()
            min_presses = sum(model[var].as_long() for var in button_vars)
            solution += min_presses

    return solution

if __name__ == "__main__":
    print(f"Solution part 1: {part1()}")
    print(f"Solution part 2: {part2()}")
