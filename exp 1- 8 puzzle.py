import heapq
import copy

# Manhattan distance heuristic function
def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                for x in range(3):
                    for y in range(3):
                        if goal[x][y] == val:
                            distance += abs(x - i) + abs(y - j)
    return distance

# Check if two states are equal
def is_goal(state, goal):
    return state == goal

# Find position of 0 (empty tile)
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate possible moves from current state
def get_neighbors(state):
    x, y = find_zero(state)
    moves = []
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # Up, Down, Left, Right
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
    return moves

# Print the puzzle state
def print_state(state):
    for row in state:
        print(" ".join(str(x) for x in row))
    print("———-")

# A* algorithm
def a_star(start, goal):
    visited = set()
    heap = []
    heapq.heappush(heap, (manhattan_distance(start, goal), 0, start, []))
    
    while heap:
        f, g, current, path = heapq.heappop(heap)
        state_tuple = tuple(tuple(row) for row in current)
        
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        
        if is_goal(current, goal):
            for step in path + [current]:
                print_state(step)
            return
        
        for neighbor in get_neighbors(current):
            if tuple(tuple(row) for row in neighbor) not in visited:
                h = manhattan_distance(neighbor, goal)
                heapq.heappush(heap, (g + 1 + h, g + 1, neighbor, path + [current]))

# Initial and goal states
start = [
    [1, 2, 3],
    [5, 6, 0],
    [7, 8, 4]
]

goal = [
    [1, 2, 3],
    [5, 8, 6],
    [0, 7, 4]
]

# Run A* algorithm
a_star(start, goal)
