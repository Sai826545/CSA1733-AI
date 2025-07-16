from collections import deque

def bfs(graph, start):
    visited = set()             # To keep track of visited nodes
    queue = deque([start])      # Use deque for efficient pops from left

    print("BFS traversal:")
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            # Add unvisited neighbors to the queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS from starting node 'A'
bfs(graph, 'A')
