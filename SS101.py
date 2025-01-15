def matrix_transpose(matrix):
    """
    Compute the transpose of a matrix.
    Time Complexity: O(rows * cols)
    Space Complexity: O(rows * cols)
    """
    if not matrix or not matrix[0]:
        return None, 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    operations = 0
    
    # Initialize result matrix with dimensions swapped
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    
    print("\nComputing Matrix Transpose:")
    print("Original Matrix:")
    print_matrix(matrix)
    
    # Compute transpose
    for i in range(rows):
        for j in range(cols):
            operations += 1
            result[j][i] = matrix[i][j]
            
            print(f"\nMoving element from position ({i},{j}) to ({j},{i}):")
            print(f"Moving {matrix[i][j]} to new position")
            print_transpose_state(matrix, result, i, j)
    
    return result, operations

def print_matrix(matrix):
    """Print matrix in a formatted way."""
    for row in matrix:
        print("[", end=" ")
        for elem in row:
            print(f"{elem:3}", end=" ")
        print("]")

def print_transpose_state(original, result, current_i, current_j):
    """Print current state of original and result matrices."""
    def print_matrix_row(matrix, row, current_i, current_j, is_original=True):
        print("[", end=" ")
        for col in range(len(matrix[row])):
            if (is_original and row == current_i and col == current_j) or \
               (not is_original and row == current_j and col == current_i):
                print(f"[{matrix[row][col]:2}]", end=" ")
            else:
                print(f"{matrix[row][col]:3}", end=" ")
        print("]")
    
    print("\nOriginal Matrix    Transposed Matrix")
    print("-" * 40)
    
    max_rows = max(len(original), len(result))
    for i in range(max_rows):
        # Print original matrix row
        if i < len(original):
            print_matrix_row(original, i, current_i, current_j)
        else:
            print(" " * 16, end="")
        
        print("   ", end="")
        
        # Print result matrix row
        if i < len(result):
            print_matrix_row(result, i, current_i, current_j, False)
        else:
            print()

def get_matrix_input():
    """Get matrix input from user."""
    try:
        rows = int(input("\nEnter number of rows: "))
        cols = int(input("Enter number of columns: "))
        
        if rows <= 0 or cols <= 0:
            print("Dimensions must be positive!")
            return None
        
        print("\nEnter matrix elements:")
        matrix = []
        for i in range(rows):
            row_input = input(f"Enter {cols} space-separated integers for row {i+1}: ")
            row = [int(x) for x in row_input.split()]
            
            if len(row) != cols:
                print(f"Error: Expected {cols} elements, got {len(row)}")
                return None
            
            matrix.append(row)
        
        return matrix
    
    except ValueError:
        print("Please enter valid integers!")
        return None

def main():
    """Test matrix transpose implementation."""
    # Get input matrix
    print("Matrix Transpose Program")
    matrix = get_matrix_input()
    if matrix is None:
        return
    
    # Perform transpose and measure time
    import time
    start_time = time.time()
    result, operations = matrix_transpose(matrix)
    end_time = time.time()
    
    if result:
        print("\nTranspose completed!")
        print(f"Operations performed: {operations}")
        print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
        
        print("\nFinal Result:")
        print("Original Matrix:")
        print_matrix(matrix)
        print("\nTransposed Matrix:")
        print_matrix(result)
        
        # Verify dimensions
        print("\nVerification:")
        print(f"Original dimensions: {len(matrix)}×{len(matrix[0])}")
        print(f"Transposed dimensions: {len(result)}×{len(result[0])}")
    else:
        print("\nError: Invalid input matrix")

if __name__ == "__main__":
    main()
