import heapq

def prim(graph, start):
    visited = set([start])
    edges = []
    for v, w in graph[start]:
        heapq.heappush(edges, (w, start, v))
    mst = []
    total = 0
    while edges:
        w, u, v = heapq.heappop(edges)
        if v in visited:
            continue
        visited.add(v)
        mst.append((u, v, w))
        total += w
        for nxt, nw in graph[v]:
            if nxt not in visited:
                heapq.heappush(edges, (nw, v, nxt))
    return mst, total

if __name__ == "__main__":
    graph = {
        'A': [('B',4), ('H',8)],
        'B': [('A',4), ('H',11), ('C',8)],
        'C': [('B',8), ('D',7), ('F',4), ('I',2)],
        'D': [('C',7), ('E',9), ('F',14)],
        'E': [('D',9), ('F',10)],
        'F': [('C',4), ('D',14), ('E',10), ('G',2)],
        'G': [('F',2), ('H',1), ('I',6)],
        'H': [('A',8), ('B',11), ('G',1), ('I',7)],
        'I': [('C',2), ('G',6), ('H',7)]
    }

    mst, cost = prim(graph, 'A')
    print("MST edges:")
    for u, v, w in mst:
        print(u, "-", v, ":", w)
    print("Total cost:", cost)
