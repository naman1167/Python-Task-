def is_symmetric(matrix):
    """
    Check if a matrix is symmetric (equal to its transpose).
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    if not matrix or not matrix[0]:
        return False, 0
    
    n = len(matrix)
    comparisons = 0
    
    # Check if matrix is square
    if any(len(row) != n for row in matrix):
        return False, comparisons
    
    print("\nChecking for Symmetry:")
    print("A matrix is symmetric if it equals its transpose (A = A^T)")
    print("This means A[i][j] = A[j][i] for all i,j")
    
    # Check symmetry: compare elements across main diagonal
    for i in range(n):
        for j in range(i+1, n):  # Only need to check upper triangle
            comparisons += 1
            print(f"\nComparing A[{i}][{j}] with A[{j}][{i}]:")
            print(f"{matrix[i][j]} {'=' if matrix[i][j] == matrix[j][i] else '≠'} {matrix[j][i]}")
            print_symmetric_check(matrix, i, j)
            
            if matrix[i][j] != matrix[j][i]:
                return False, comparisons
    
    return True, comparisons

def print_matrix(matrix):
    """Print matrix in a formatted way."""
    for row in matrix:
        print("[", end=" ")
        for elem in row:
            print(f"{elem:3}", end=" ")
        print("]")

def print_symmetric_check(matrix, pos1_i, pos1_j):
    """Print matrix with highlighted elements being compared."""
    n = len(matrix)
    print("\nCurrent state:")
    for i in range(n):
        print("[", end=" ")
        for j in range(n):
            if (i == pos1_i and j == pos1_j) or (i == pos1_j and j == pos1_i):
                print(f"[{matrix[i][j]:2}]", end=" ")
            else:
                print(f"{matrix[i][j]:3}", end=" ")
        print("]")

def get_matrix_input():
    """Get square matrix input from user."""
    try:
        n = int(input("\nEnter size of square matrix: "))
        
        if n <= 0:
            print("Size must be positive!")
            return None
        
        print("\nEnter matrix elements:")
        matrix = []
        for i in range(n):
            row_input = input(f"Enter {n} space-separated integers for row {i+1}: ")
            row = [int(x) for x in row_input.split()]
            
            if len(row) != n:
                print(f"Error: Expected {n} elements, got {len(row)}")
                return None
            
            matrix.append(row)
        
        return matrix
    
    except ValueError:
        print("Please enter valid integers!")
        return None

def main():
    """Test symmetric matrix checker."""
    print("Symmetric Matrix Checker")
    print("A matrix is symmetric if it equals its transpose")
    
    # Get input matrix
    matrix = get_matrix_input()
    if matrix is None:
        return
    
    # Print original matrix
    print("\nInput Matrix:")
    print_matrix(matrix)
    
    # Check symmetry and measure time
    import time
    start_time = time.time()
    is_sym, comparisons = is_symmetric(matrix)
    end_time = time.time()
    
    # Print results
    print("\nAnalysis completed!")
    print(f"Comparisons made: {comparisons}")
    print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
    
    if is_sym:
        print("\nResult: Matrix IS symmetric!")
        print("This means A[i][j] = A[j][i] for all i,j")
    else:
        print("\nResult: Matrix is NOT symmetric!")
        print("Found elements that don't match across the main diagonal")
    
    # Additional properties if symmetric
    if is_sym:
        # Check diagonal elements
        print("\nDiagonal elements:")
        for i in range(len(matrix)):
            print(f"A[{i}][{i}] = {matrix[i][i]}")
        
        # Check if diagonal symmetric
        is_diag_sym = all(matrix[i][i] == matrix[0][0] for i in range(len(matrix)))
        if is_diag_sym:
            print("\nNote: All diagonal elements are equal!")

if __name__ == "__main__":
    main()
