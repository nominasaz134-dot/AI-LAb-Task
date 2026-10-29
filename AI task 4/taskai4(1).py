import heapq
from itertools import count

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}
def astar(graph, h, start, goal):
    serial = count()
    pq = [(h[start], 0, next(serial), start, [start])]
    best_g = {start: 0}
    processed = []
    expanded = []
    while pq:
        f, g, _, node, path = heapq.heappop(pq)
        if g != best_g.get(node):
            continue
        processed.append((node, g, h[node], f))
        if node == goal:
            return path, g, processed, expanded
        expanded.append(node)  # goal excluded from expansion count
        for nxt, w in graph.get(node, []):
            ng = g + w
            if ng < best_g.get(nxt, float("inf")):
                best_g[nxt] = ng
                heapq.heappush(
                    pq, (ng + h[nxt], ng, next(serial), nxt, path + [nxt])
                )
    return None, float("inf"), processed, expanded
h_original = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}
h_overestimate = {"S": 5, "A": 4, "B": 4, "C": 10, "G": 0}
print("Original:", astar(graph, h_original, "S", "G"))
print("Overestimate:", astar(graph, h_overestimate, "S", "G"))
