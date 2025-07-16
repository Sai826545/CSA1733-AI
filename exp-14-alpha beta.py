# Alpha-Beta Pruning Algorithm Implementation

import math

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        max_eval = -math.inf
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Example usage
if __name__ == "__main__":
    root = Node(0)
    child1 = Node(3)
    child2 = Node(5)
    child3 = Node(6)
    child4 = Node(9)
    child5 = Node(1)
    child6 = Node(2)

    root.children = [child1, child2, child3]
    child1.children = [Node(3), Node(5)]
    child2.children = [Node(6), Node(9)]
    child3.children = [Node(1), Node(2)]

    depth = 3
    result = alpha_beta(root, depth, -math.inf, math.inf, True)
    print("Optimal value:", result)
