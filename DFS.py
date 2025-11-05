class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                self.dfs(neighbour, visited)

g = Graph()
edges = [(0,1), (0,2), (1,3), (1,4), (2,5), (5,6)]
for u, v in edges:
    g.add_edge(u, v)

visited = set()
print("DFS Traversal:")
g.dfs(0, visited)
