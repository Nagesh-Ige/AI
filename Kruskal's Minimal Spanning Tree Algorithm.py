# Kruskal's algorithm for Minimum Spanning Tree

class UnionFind:
    def __init__(self, nodes):
        self.parent = {n: n for n in nodes}
        self.rank = {n: 0 for n in nodes}
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True

def kruskal(edges):
    nodes = {u for u, v, _ in edges} | {v for u, v, _ in edges}
    uf = UnionFind(nodes)
    mst = []
    total = 0
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if uf.union(u, v):
            mst.append((u, v, w))
            total += w
    return mst, total

if __name__ == "__main__":
    edges = [
        ('A','B',4), ('A','H',8), ('B','H',11), ('B','C',8),
        ('C','D',7), ('C','F',4), ('C','I',2), ('D','E',9),
        ('D','F',14), ('E','F',10), ('F','G',2), ('G','H',1),
        ('G','I',6), ('H','I',7)
    ]

    mst, cost = kruskal(edges)
    print("MST edges:")
    for u, v, w in mst:
        print(f"{u} - {v} : {w}")
    print("Total cost:", cost)
