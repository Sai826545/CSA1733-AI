from collections import deque

# State representation: (missionaries_left, cannibals_left, boat_position)
# boat_position: 0 means left side, 1 means right side
def is_valid(state):
    m_left, c_left, _ = state
    m_right, c_right = 3 - m_left, 3 - c_left

    # No side should have negative values
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False

    # Missionaries should not be outnumbered on either side
    if (m_left > 0 and m_left < c_left) or (m_right > 0 and m_right < c_right):
        return False

    return True

def get_successors(state):
    successors = []
    m, c, b = state
    direction = -1 if b == 0 else 1

    # All possible moves: combinations of 1 or 2 persons in the boat
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    for m_move, c_move in moves:
        new_state = (
            m + direction * m_move,
            c + direction * c_move,
            1 - b
        )
        if is_valid(new_state):
            successors.append(new_state)
    return successors

def bfs(start, goal):
    queue = deque()
    queue.append((start, [start]))
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path

        for successor in get_successors(state):
            queue.append((successor, path + [successor]))
    return None

def main():
    start = (3, 3, 0)
    goal = (0, 0, 1)
    solution = bfs(start, goal)

    if solution:
        print("Solution found in", len(solution)-1, "moves:")
        for step in solution:
            print(step)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
