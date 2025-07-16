def print_grid(grid):
    for row in grid:
        print(row)

def vacuum_cleaner(grid):
    print("All the room are dirty")
    initial_dirty = [[1, 1, 1, 1] for _ in range(4)]
    print_grid(initial_dirty)

    print("Before cleaning the room I detect all of this")
    print_grid(grid)

    cleaned_cells = 0
    total_cells = 16

    # Define vacuum cleaner path (manually or systematically)
    path = [
        (0, 0), (0, 2), (0, 3),
        (1, 3), (2, 0)
    ]

    for x, y in path:
        print(f"Vacuum in location now, {x} {y}")
        if grid[x][y] == 1:
            grid[x][y] = 0
            cleaned_cells += 1
            print(f"Cleaned {x} {y}")
        else:
            print(f"{x} {y} is already clean")

    print("Room is clean now,")
    print("a = safaRat cleaner")
    print_grid(grid)

    performance = (cleaned_cells / total_cells) * 100
    print(f"Performance: {performance:.2f}%")

# Define initial dirty state
room = [
    [1, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 0, 0]
]

vacuum_cleaner(room)
