def solve_n_queens(n):
    """
    Solve N-Queens puzzle using backtracking.
    Time Complexity: O(N!)
    Space Complexity: O(N)
    """
    def is_safe(board, row, col):
        """Check if a queen can be placed on board[row][col]."""
        # Check row on left side
        for j in range(col):
            if board[row][j] == 'Q':
                return False
        
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check lower diagonal on left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        return True

    def solve(board, col):
        """Recursive utility function to solve N-Queens."""
        nonlocal solutions, steps
        
        if col >= n:
            solutions.append([row[:] for row in board])
            print("\nFound solution:")
            print_board(board)
            return True
        
        result = False
        for i in range(n):
            steps += 1
            if is_safe(board, i, col):
                # Place queen
                board[i][col] = 'Q'
                print(f"\nStep {steps}: Trying queen at position ({i}, {col})")
                print_board(board)
                
                # Recur to place rest of the queens
                solve(board, col + 1)
                
                # Backtrack
                board[i][col] = '.'
                print(f"\nBacktracking from position ({i}, {col})")
                print_board(board)
        
        return result

    # Initialize empty board
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    steps = 0
    
    print(f"\nSolving {n}-Queens Puzzle:")
    solve(board, 0)
    
    return solutions, steps

def print_board(board):
    """Print the chess board."""
    n = len(board)
    print("\n  " + " ".join(str(i) for i in range(n)))
    for i in range(n):
        print(f"{i} ", end="")
        for j in range(n):
            if board[i][j] == 'Q':
                print("♛ ", end="")
            else:
                print(". ", end="")
        print()

def analyze_solutions(solutions, n):
    """Analyze the N-Queens solutions."""
    if not solutions:
        print("\nNo solutions found!")
        return
    
    print("\nSolution Analysis:")
    print(f"Total solutions found: {len(solutions)}")
    
    # Verify solutions
    valid_solutions = 0
    for solution in solutions:
        if is_valid_solution(solution):
            valid_solutions += 1
    
    print(f"Valid solutions: {valid_solutions}")
    
    # Known solutions for small N
    known_solutions = {1: 1, 2: 0, 3: 0, 4: 2, 5: 10, 6: 4, 7: 40, 8: 92}
    if n in known_solutions:
        print(f"Expected solutions for n={n}: {known_solutions[n]}")
    
    # Show first solution details
    if solutions:
        print("\nFirst solution details:")
        print_solution_stats(solutions[0])

def is_valid_solution(board):
    """Verify if a solution is valid."""
    n = len(board)
    
    # Check rows and columns
    for i in range(n):
        row_count = sum(1 for j in range(n) if board[i][j] == 'Q')
        col_count = sum(1 for j in range(n) if board[j][i] == 'Q')
        if row_count != 1 or col_count != 1:
            return False
    
    # Check diagonals
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'Q':
                # Check diagonals from this queen
                for k in range(1, n):
                    # Check all 4 diagonal directions
                    directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
                    for di, dj in directions:
                        ni, nj = i + di*k, j + dj*k
                        if 0 <= ni < n and 0 <= nj < n:
                            if board[ni][nj] == 'Q':
                                return False
    return True

def print_solution_stats(board):
    """Print statistics about a solution."""
    n = len(board)
    queens = [(i,j) for i in range(n) for j in range(n) if board[i][j] == 'Q']
    
    print("Queen positions:", end=" ")
    for i, j in queens:
        print(f"({i},{j})", end=" ")
    print()
    
    # Calculate distances between queens
    print("\nQueen distances:")
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            x1, y1 = queens[i]
            x2, y2 = queens[j]
            dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
            print(f"Queens at ({x1},{y1}) and ({x2},{y2}): {dist:.2f}")

def get_user_input():
    """Get board size from user."""
    try:
        n = int(input("Enter the size of the board (N): "))
        if n <= 0:
            print("Board size must be positive!")
            return None
        
        if n > 12:
            print("Warning: Large board size!")
            print("This may take a very long time to solve.")
            proceed = input("Continue? (y/n): ").lower()
            if proceed != 'y':
                return None
        
        return n
    
    except ValueError:
        print("Please enter a valid integer!")
        return None

def main():
    """Test N-Queens implementation."""
    # Get input
    n = get_user_input()
    if n is None:
        return
    
    print(f"\nSolving {n}-Queens puzzle...")
    
    # Solve puzzle and measure time
    import time
    start_time = time.time()
    solutions, steps = solve_n_queens(n)
    end_time = time.time()
    
    # Print results
    print("\nSolving completed!")
    print(f"Steps performed: {steps}")
    print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
    
    analyze_solutions(solutions, n)

if __name__ == "__main__":
    main()
