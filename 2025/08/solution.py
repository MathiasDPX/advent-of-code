import math
import itertools
import heapq

data = open("input.txt", "r").read().splitlines()


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
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
    for i, j in itertools.combinations(range(len(points)), 2):
        yield (math.dist(points[i], points[j]), i, j)


edges = heapq.nsmallest(1000, edge_iter(), key=lambda x: x[0])

dsu = DSU(len(points))
connections = 0
for _, a, b in edges:
    if dsu.union(a, b):
        connections += 1
        if connections == 1000:
            break

component_sizes = []
for i in range(len(points)):
    if dsu.find(i) == i:
        component_sizes.append(dsu.size[i])

component_sizes.sort(reverse=True)
top3 = (component_sizes + [1, 1, 1])[:3]
print(top3[0] * top3[1] * top3[2])
