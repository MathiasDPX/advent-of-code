import math
import itertools
import heapq

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


def part1():
    # extract the 1000 shortest edges
    edges = heapq.nsmallest(1000, edge_iter(), key=lambda x: x[0])

    # process edges in order of increasing distance
    dsu = DSU(len(points))
    connections = 0
    for _, a, b in edges:
        if dsu.union(a, b):
            connections += 1
            if connections == 1000:
                break

    # Part 1: multiply together the sizes of the three largest circuits
    dsu.size.sort(reverse=True)
    top3 = dsu.size[:3]
    
    return top3[0] * top3[1] * top3[2]


def part2():
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

    return points[last_a][0] * points[last_b][0]


if __name__ == "__main__":
    print(f"Solution part 1: {part1()}")
    print(f"Solution part 2: {part2()}")
