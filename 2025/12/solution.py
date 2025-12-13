import re

data = open("input.txt", "r").read()

SHAPE_PATTERN = r"(?:^|\n)([#.]+(?:\n[#.]+)*)"
REGION_PATTERN = r"(\d+)x(\d+):\s*([0-9 ]+)"

shapes = []
for match in re.finditer(SHAPE_PATTERN, data):
    shape = match.group(1).strip()
    shape = shape.splitlines()

    shape = [[char == "#" for char in list(line)] for line in shape]
    shapes.append(shape)

regions = []
for match in re.finditer(REGION_PATTERN, data):
    region = {}
    size = (int(match.group(1)), int(match.group(2)))
    shapes_count = list(map(int, match.group(3).split(" ")))

    region["size"] = size
    region["shapes"] = shapes_count

    regions.append(region)


def rotate_shape(shape, angle):
    def rot90(shp):
        return [list(row)[::-1] for row in zip(*shp)]

    turns = (angle // 90) % 4
    result = shape
    for _ in range(turns):
        result = rot90(result)
    return result


def mirror_shape(shape, vertical):
    if vertical:
        return [row[::-1] for row in shape]
    else:
        return shape[::-1]


def shape_cells(shape):
    return sum(1 for row in shape for c in row if c)


def normalize_shape(shape):
    # convert map of bool to map of tuple of int
    return tuple(tuple(int(c) for c in row) for row in shape)


def unique_orientations(shape):
    # generate all rotations and mirrors
    variants = []
    for angle in (0, 90, 180, 270):
        rot = rotate_shape(shape, angle)
        variants.append(rot)
        variants.append(mirror_shape(rot, vertical=True))
        variants.append(mirror_shape(rot, vertical=False))

    seen = set()
    uniq = []
    for var in variants:
        canon = normalize_shape(var)
        if canon not in seen:
            seen.add(canon)
            uniq.append([[bool(c) for c in row] for row in canon])
    return uniq


def can_place(grid, w, h, shp, x, y):
    sh = len(shp)
    sw = len(shp[0])
    if x + sw > w or y + sh > h:
        return False

    # ensure no overlap on cells
    for dy in range(sh):
        for dx in range(sw):
            if shp[dy][dx] and grid[y + dy][x + dx]:
                return False
    return True


def place_shape(grid, shp, x, y):
    sh = len(shp)
    sw = len(shp[0])
    for dy in range(sh):
        for dx in range(sw):
            if shp[dy][dx]:
                grid[y + dy][x + dx] = True


def remove_shape(grid, shp, x, y):
    sh = len(shp)
    sw = len(shp[0])
    for dy in range(sh):
        for dx in range(sw):
            if shp[dy][dx]:
                grid[y + dy][x + dx] = False


def search_region(w, h, shapes_counts, shapes_orients, areas):
    total = sum(areas[i] * shapes_counts[i] for i in range(len(shapes_counts)))
    if total > w * h:
        return False

    # order pieces by descending area to reduce branching
    piece_list = []
    for i, cnt in enumerate(shapes_counts):
        for _ in range(cnt):
            piece_list.append(i)
    piece_list.sort(key=lambda idx: areas[idx], reverse=True)

    grid = [[False] * w for _ in range(h)]

    def backtrack(pi):
        if pi == len(piece_list):
            return True
        idx = piece_list[pi]
        for shp in shapes_orients[idx]:
            sh = len(shp)
            sw = len(shp[0])

            for y in range(h - sh + 1):
                for x in range(w - sw + 1):
                    if not can_place(grid, w, h, shp, x, y):
                        continue
                    place_shape(grid, shp, x, y)
                    if backtrack(pi + 1):
                        return True
                    remove_shape(grid, shp, x, y)
        return False

    return backtrack(0)


def part1():
    # precompute orientations and areas for each shape index
    orientations = [unique_orientations(s) for s in shapes]
    areas = [shape_cells(s) for s in shapes]

    count_fit = 0
    regions_count = len(regions)

    for i, region in enumerate(regions):
        w, h = region["size"]
        needed = region["shapes"]
        needed = needed[: len(shapes)]
        if search_region(w, h, needed, orientations, areas):
            count_fit += 1

        if i % 50 == 0:
            print(f"{i}/{regions_count}")
    return count_fit


print(part1())
