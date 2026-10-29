
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}

FOUND = "FOUND"
CUTOFF = "CUTOFF"
FAILURE = "FAILURE"


def dls(start, goal, limit):

    def visit(node, depth, path):
        if node == goal:
            return FOUND, path

        if depth == limit:
            return (CUTOFF, None) if graph[node] else (FAILURE, None)

        saw_cutoff = False

        for nxt in graph[node]:
            if nxt in path:
                continue

            status, result_path = visit(
                nxt, depth + 1, path + [nxt]
            )

            if status == FOUND:
                return FOUND, result_path

            if status == CUTOFF:
                saw_cutoff = True

        return (CUTOFF, None) if saw_cutoff else (FAILURE, None)

    return visit(start, 0, [start])


def iddfs(start, goal, max_depth):
    attempts = []

    for limit in range(max_depth + 1):
        status, path = dls(start, goal, limit)
        attempts.append((limit, status, path))

        if status == FOUND:
            return status, path, attempts

        if status == FAILURE:
            return status, None, attempts

    return CUTOFF, None, attempts


for limit in (1, 2, 3, 4):
    status, path = dls("A", "G", limit)
    print(f"DLS limit={limit}: status={status}, path={path}")


for max_depth in (1, 2, 3, 4):
    status, path, attempts = iddfs("A", "G", max_depth)

    print(
        f"IDDFS max_depth={max_depth}: status={status}, "
        f"path={path}, limits_attempted={[x[0] for x in attempts]}"
    )
