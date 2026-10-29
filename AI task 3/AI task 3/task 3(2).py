
from collections import deque
import heapq
from itertools import count

weighted_graph = {
    "A": [("B", 1), ("C", 2)],
    "B": [("D", 5), ("E", 1)],
    "C": [("F", 5), ("G", 10)],
    "D": [],
    "E": [("G", 1)],
    "F": [],
    "G": []
}


def ucs(start, goal):
    serial = count()
    frontier = [(0, next(serial), start, [start])]
    best_cost = {start: 0}
    processed = []

    while frontier:
        cost, _, node, path = heapq.heappop(frontier)

        if cost != best_cost.get(node):
            continue

        processed.append((node, cost))

        if node == goal:
            return path, cost, processed

        for nxt, edge_cost in weighted_graph[node]:
            new_cost = cost + edge_cost

            if new_cost < best_cost.get(nxt, float("inf")):
                best_cost[nxt] = new_cost

                heapq.heappush(
                    frontier,
                    (new_cost, next(serial), nxt, path + [nxt])
                )

    return None, float("inf"), processed


def bfs(start, goal):
    graph = {
        node: [nxt for nxt, _ in edges]
        for node, edges in weighted_graph.items()
    }

    q = deque([(start, [start])])
    seen = {start}
    processed = []

    while q:
        node, path = q.popleft()
        processed.append(node)

        if node == goal:
            cost = sum(
                next(w for nxt, w in weighted_graph[u] if nxt == v)
                for u, v in zip(path, path[1:])
            )
            return path, cost, processed

        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                q.append((nxt, path + [nxt]))

    return None, float("inf"), processed


ucs_path, ucs_cost, ucs_order = ucs("A", "G")
bfs_path, bfs_cost, bfs_order = bfs("A", "G")

print("UCS path:", ucs_path)
print("UCS cost:", ucs_cost)
print("UCS processing order:", ucs_order)

print("BFS path:", bfs_path)
print("BFS cost:", bfs_cost)
print("BFS processing order:", bfs_order)
