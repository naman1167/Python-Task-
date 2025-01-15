from collections import deque

def shortest_path_grid(grid):
    """
    Find shortest path in grid from top-left to bottom-right using BFS.
    Time Complexity: O(rows * cols)
    Space Complexity: O(rows * cols)
    """
    if not grid or not grid[0]:
        return None, 0
    
    rows, cols = len(grid), len(grid[0])
    # Directions: right and down only
    directions = [(0, 1), (1, 0)]
    
    # Queue for BFS: (row, col, path, steps)
    queue = deque([(0, 0, [(0, 0)], 0)])
    # Keep track of visited cells
    visited = {(0, 0)}
    steps = 0
    
    print("\nFinding shortest path using BFS:")
    print("Start: (0, 0)")
    print("Target: ({}, {})".format(rows-1, cols-1))
    print_grid(grid, [(0, 0)], visited)
    
    while queue:
        row, col, path, distance = queue.popleft()
        steps += 1
        
        if row == rows-1 and col == cols-1:
            return path, steps
        
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                grid[new_row][new_col] != '#' and 
                (new_row, new_col) not in visited):
                
                new_path = path + [(new_row, new_col)]
                queue.append((new_row, new_col, new_path, distance + 1))
                visited.add((new_row, new_col))
                
                print(f"\nStep {steps}: Moving to ({new_row}, {new_col})")
                print_grid(grid, new_path, visited)
    
    return None, steps

def print_grid(grid, path, visited):
    """Print grid with path and visited cells."""
    rows, cols = len(grid), len(grid[0])
    
    print("\nCurrent state:")
    print("  " + " ".join(str(i) for i in range(cols)))
    
    for i in range(rows):
        print(f"{i} ", end="")
        for j in range(cols):
            if (i, j) == path[-1]:  # Current position
                print("@ ", end="")
            elif (i, j) in path:  # Path
                print("* ", end="")
            elif (i, j) in visited:  # Visited
                print("· ", end="")
            elif grid[i][j] == '#':  # Wall
                print("# ", end="")
            else:  # Unvisited
                print(". ", end="")
        print()

def analyze_path(path, grid):
    """Analyze the found path."""
    if not path:
        return
    
    print("\nPath Analysis:")
    print(f"Path length: {len(path)}")
    print("Path coordinates:", path)
    
    # Calculate Manhattan distance
    start = path[0]
    end = path[-1]
    manhattan_dist = abs(end[0] - start[0]) + abs(end[1] - start[1])
    print(f"Manhattan distance: {manhattan_dist}")
    
    # Check if path is optimal
    is_optimal = len(path) == manhattan_dist + 1
    print("Path is optimal:", "Yes" if is_optimal else "No")
    
    # Analyze turns in path
    turns = 0
    for i in range(1, len(path)-1):
        prev_dir = (path[i][0] - path[i-1][0], path[i][1] - path[i-1][1])
        next_dir = (path[i+1][0] - path[i][0], path[i+1][1] - path[i][1])
        if prev_dir != next_dir:
            turns += 1
    print(f"Number of turns: {turns}")

def get_user_input():
    """Get grid dimensions and walls from user."""
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
        
        if rows <= 0 or cols <= 0:
            print("Dimensions must be positive!")
            return None
        
        # Initialize empty grid
        grid = [['.' for _ in range(cols)] for _ in range(rows)]
        
        # Get wall positions
        print("\nEnter wall positions (row col), one per line.")
        print("Enter 'done' when finished:")
        while True:
            pos = input()
            if pos.lower() == 'done':
                break
            
            try:
                r, c = map(int, pos.split())
                if 0 <= r < rows and 0 <= c < cols:
                    grid[r][c] = '#'
                else:
                    print("Position out of bounds!")
            except ValueError:
                print("Invalid input! Use format: row col")
        
        return grid
    
    except ValueError:
        print("Please enter valid integers!")
        return None

def main():
    """Test shortest path implementation."""
    print("Shortest Path in Grid")
    print("Find path from top-left to bottom-right")
    print("Moving only right or down")
    
    # Get input grid
    grid = get_user_input()
    if grid is None:
        return
    
    print("\nInitial Grid:")
    print_grid(grid, [(0, 0)], set())
    
    # Find path and measure time
    import time
    start_time = time.time()
    path, steps = shortest_path_grid(grid)
    end_time = time.time()
    
    # Print results
    print("\nSearch completed!")
    print(f"Steps performed: {steps}")
    print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
    
    if path:
        print("\nPath found!")
        print("Final grid state:")
        print_grid(grid, path, set())
        analyze_path(path, grid)
    else:
        print("\nNo path exists!")
        print("The target is unreachable from the start position")

if __name__ == "__main__":
    main()
