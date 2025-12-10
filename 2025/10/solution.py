import itertools
import re

BUTTONS_PATTERN = r"\(([^)]*)\)"

data = open("input.txt", "r").read().splitlines()


class LightMachine:
    def __init__(self, line):
        self.target_lights = line.split("]")[0][1:]
        self.target_lights = [char == "#" for char in self.target_lights]
        self.lights = [False] * len(self.target_lights)

        self.buttons = []
        for match in re.finditer(BUTTONS_PATTERN, line):
            keys_str = match.group(1)
            if keys_str:
                keys = [int(key) for key in keys_str.split(",")]
            else:
                keys = []
            self.buttons.append(tuple(keys))

    def press(self, index):
        button = self.buttons[index]
        for key in button:
            self.lights[key] = not self.lights[key]

    def reset(self):
        self.lights = [False] * len(self.target_lights)

    def check(self):
        return self.lights == self.target_lights

    def bruteforce(self, press):
        for combo in itertools.product(range(len(self.buttons)), repeat=press):
            self.reset()

            for button_index in combo:
                self.press(button_index)
            if self.check():
                return True

        return False


lightmachines = []
for line in data:
    lightmachines.append(LightMachine(line))


def part1():
    solution = 0
    for machine in lightmachines:
        success = False
        press = 1
        while not success:
            success = machine.bruteforce(press)

            if not success:
                press += 1

        solution += press

    return solution


print(f"Solution part 1: {part1()}")
