import math
import itertools

data = open("input.txt", "r").read().splitlines()


class DSU:
    # disjoint set union

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        # find parent of element x
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        # union two circuits
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


points = [tuple(map(int, line.split(","))) for line in data]


def edge_iter():
    # yield all possible edges as (distance, point_a, point_b)
    for i, j in itertools.combinations(range(len(points)), 2):
        yield (math.dist(points[i], points[j]), i, j)


edges = list(edge_iter())
edges.sort()

# process edges in order of increasing distance
dsu = DSU(len(points))
connections = 0
last_a, last_b = None, None
for _, a, b in edges:
    if dsu.union(a, b):
        connections += 1
        last_a, last_b = a, b
        if connections == len(points) - 1:
            break

component_sizes = []
for i in range(len(points)):
    if dsu.find(i) == i:
        component_sizes.append(dsu.size[i])

print("Solution part 2:", points[last_a][0] * points[last_b][0])