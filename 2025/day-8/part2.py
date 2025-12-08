class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i):
        while self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return False

        a_size = self.size[rootA]
        b_size = self.size[rootB]

        if a_size < b_size:
            self.parent[rootA] = rootB
            self.size[rootB] += a_size
        else:
            self.parent[rootB] = rootA
            self.size[rootA] += b_size

        return True


def dist_squared(a, b):
    return sum((a[i] - b[i]) ** 2 for i in range(len(a)))


with open('input.txt') as f:
    points = [[int(i) for i in line.strip().split(",")] for line in f.readlines()]


edges = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        d = dist_squared(points[i], points[j])
        edges.append((d, i, j))


uf = UnionFind(len(points))
last_joined = None
for d, i, j in sorted(edges):
    if uf.union(i, j):
        last_joined = (i, j)

print(eval("*".join(str(points[i][0]) for i in last_joined)))
