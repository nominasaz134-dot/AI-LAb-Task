
import math
def minimax(depth, index, is_max, scores, target_depth, counter):
    if depth == target_depth:
        counter["leaves"] += 1
        return scores[index]
    if is_max:
        return max(
            minimax(depth + 1, index * 2, False, scores,
                    target_depth, counter),

            minimax(depth + 1, index * 2 + 1, False, scores,
                    target_depth, counter)
        )
    else:
        return min(
            minimax(depth + 1, index * 2, True, scores,
                    target_depth, counter),

            minimax(depth + 1, index * 2 + 1, True, scores,
                    target_depth, counter)
        )
def alphabeta(depth, index, is_max, scores, target_depth,
              alpha, beta, counter):
    if depth == target_depth:
        counter["leaves"] += 1
        return scores[index]
    if is_max:
        value = float("-inf")
        for i in range(2):
            value = max(
                value,
                alphabeta(
                    depth + 1, index * 2 + i, False,
                    scores, target_depth, alpha, beta, counter
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
                    scores, target_depth, alpha, beta, counter
                )
            )
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
scores = [3, 5, 2, 9, 0, 7, 0, 0]
depth = int(math.log2(len(scores)))
minimax_count = {"leaves": 0}
minimax_value = minimax(
    0, 0, True, scores, depth, minimax_count
)
alphabeta_count = {"leaves": 0}
alphabeta_value = alphabeta(
    0, 0, True, scores, depth,
    float("-inf"), float("inf"), alphabeta_count
)
print("Minimax value:", minimax_value)
print("Minimax leaves evaluated:", minimax_count["leaves"])
print("Alpha-Beta value:", alphabeta_value)
print("Alpha-Beta leaves evaluated:", alphabeta_count["leaves"])
