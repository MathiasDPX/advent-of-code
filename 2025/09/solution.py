from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely.geometry import box
import itertools
import time

data = open("input.txt", "r").read().splitlines()

raw_points = []
points = []

for line in data:
    x, y = line.split(",")
    x, y = int(x), int(y)
    raw_points.append((x, y))
    points.append(Point(x, y))


def part1():
    maxarea = 0

    for a, b in itertools.combinations(raw_points, 2):
        if a == b:
            continue

        width = abs(a[0] - b[0]) + 1
        height = abs(a[1] - b[1]) + 1
        area = width * height

        maxarea = max(maxarea, area)

    return maxarea


def part2():
    polygon = Polygon(points)
    maxarea = 0

    for a, b in itertools.combinations(raw_points, 2):
        if a == b:
            continue

        minx, maxx = sorted((a[0], b[0]))
        miny, maxy = sorted((a[1], b[1]))

        rect = box(minx, miny, maxx, maxy)
        if not polygon.covers(rect):
            continue

        width = maxx - minx + 1
        height = maxy - miny + 1
        area = width * height

        maxarea = max(maxarea, area)

    return maxarea


def timeit(func):
    start = time.time()
    solution = func()
    end = time.time()

    return (end - start, solution)


duration, solution = timeit(part1)
print(f"Solution part 1: {solution} in {duration:.2f}ms")

duration, solution = timeit(part2)
print(f"Solution part 2: {solution} in {duration:.2f}ms")