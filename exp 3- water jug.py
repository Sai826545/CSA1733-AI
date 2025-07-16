from collections import deque

# Jug capacities
jug1_capacity = 4
jug2_capacity = 3
target = 2

# To store visited states
visited = set()

# To store the path
def is_goal(state):
    x, y = state
    return x == target or y == target

def get_next_states(x, y):
    return [
        (jug1_capacity, y),    # Fill Jug1
        (x, jug2_capacity),    # Fill Jug2
        (0, y),                # Empty Jug1
        (x, 0),                # Empty Jug2
        (x - min(x, jug2_capacity - y), y + min(x, jug2_capacity - y)),  # Pour Jug1 -> Jug2
        (x + min(y, jug1_capacity - x), y - min(y, jug1_capacity - x))   # Pour Jug2 -> Jug1
    ]

def bfs():
    queue = deque()
    parent = {}
    start = (0, 0)
    queue.append(start)
    visited.add(start)
    parent[start] = None

    while queue:
        state = queue.popleft()
        if is_goal(state):
            path = []
            while state:
                path.append(state)
                state = parent[state]
            path.reverse()
            print("Path of states by jugs:")
            for s in path:
                print(f"{s[0]},{s[1]}")
            return

        for next_state in get_next_states(*state):
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = state
                queue.append(next_state)

bfs()
