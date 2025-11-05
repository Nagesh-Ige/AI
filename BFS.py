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

    def bfs_recursive(self, queue, visited):
        if not queue:
            return
        node = queue.pop(0)
        print(node, end=" ")
        for neighbour in self.graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
        self.bfs_recursive(queue, visited)

    def bfs(self, start):
        visited = set([start])
        queue = [start]
        self.bfs_recursive(queue, visited)


g = Graph()
edges = [(0,1), (0,2), (1,3), (1,4), (2,5), (5,6)]
for u, v in edges:
    g.add_edge(u, v)

print("BFS Traversal:")
g.bfs(0)
