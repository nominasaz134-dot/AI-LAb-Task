
def minimax(depth, index, is_max, scores, target, counter):
    if depth == target:
        counter["leaves"] += 1
        return scores[index]
    if is_max:
        return max(
            minimax(depth + 1, index * 2, False, scores, target, counter),
            minimax(depth + 1, index * 2 + 1, False, scores, target, counter)
        )
    else:
        return min(
            minimax(depth + 1, index * 2, True, scores, target, counter),
            minimax(depth + 1, index * 2 + 1, True, scores, target, counter)
        )
def alphabeta(depth, index, is_max, scores, target,
              alpha, beta, counter):
    if depth == target:
        counter["leaves"] += 1
        return scores[index]
    if is_max:
        value = float("-inf")
        for i in range(2):
            value = max(
                value,
                alphabeta(
                    depth + 1, index * 2 + i, False,
                    scores, target, alpha, beta, counter
                )
            )
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float("inf")
        for i in range(2):
            value = min(
                value,
                alphabeta(
                    depth + 1, index * 2 + i, True,
                    scores, target, alpha, beta, counter
                )
            )
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
def compare_order(scores):
    depth = 3
    mm_count = {"leaves": 0}
    ab_count = {"leaves": 0}
    mm_value = minimax(
        0, 0, True, scores, depth, mm_count
    )
    ab_value = alphabeta(
        0, 0, True, scores, depth,
        float("-inf"), float("inf"), ab_count
    )
    print("Leaves:", scores)
    print("Minimax value:", mm_value)
    print("Minimax leaves evaluated:", mm_count["leaves"])
    print("Alpha-Beta value:", ab_value)
    print("Alpha-Beta leaves evaluated:", ab_count["leaves"])
    print()
original = [3, 5, 2, 9, 0, 7, 0, 0]
reordered = [2, 9, 3, 5, 0, 0, 0, 7]
compare_order(original)
compare_order(reordered)
