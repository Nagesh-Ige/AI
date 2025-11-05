import heapq

def a_star(start, goal, graph, heuristic):
    open_list = [(0 + heuristic[start], 0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_list:
        f, g, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph[current]:
            new_g = g + cost
            if neighbor not in g_score or new_g < g_score[neighbor]:
                g_score[neighbor] = new_g
                f_score = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_score, new_g, neighbor))
                came_from[neighbor] = current

    return None

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 3), ('E', 1)],
    'C': [('A', 3), ('F', 5)],
    'D': [('B', 3), ('E', 1), ('G', 2)],
    'E': [('B', 1), ('D', 1), ('G', 3)],
    'F': [('C', 5), ('G', 2)],
    'G': [('D', 2), ('E', 3), ('F', 2)]
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 0
}

path = a_star('A', 'G', graph, heuristic)
print("Path:", path)
