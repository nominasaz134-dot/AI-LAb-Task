import heapq
from itertools import count
from tracemalloc import start

graph = {
"S": [("A", 1), ("B", 4)],
"A": [("C", 2)],
"B": [("G", 5)],
"C": [("G", 3)],
"G": []
}
heuristic = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}

def best_first_search(graph, h, start, goal):
    serial = count()
    # Queue item: (f, g, insertion_order, node, path)
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

        expanded.append(node)  
        for nxt, w in graph.get(node, []):
            ng = g + w
            if ng < best_g.get(nxt, float("inf")):
                best_g[nxt] = ng
                heapq.heappush(
                    pq, (ng + h[nxt], ng, next(serial), nxt, path + [nxt])
                )
    return None, float("inf"), processed, expanded


astar_result = best_first_search(graph, heuristic, "S", "G")
ucs_heuristic = {node: 0 for node in graph}
ucs_result = best_first_search(graph, ucs_heuristic, "S", "G")

for name, result in [("A*", astar_result), ("UCS", ucs_result)]:
    path, cost, processed, expanded = result
    print(name, "path =", path, "cost =", cost)
    print(name, "processed =", processed)
    print(name, "expanded =", expanded, "count =", len(expanded))
