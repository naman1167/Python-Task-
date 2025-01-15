def matrix_addition(matrix1, matrix2):
    """
    Add two matrices of the same dimensions.
    Returns the resulting matrix and number of operations performed.
    """
    if not (matrix1 and matrix2 and matrix1[0] and matrix2[0]):
        return None, 0
    
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    
    # Check if matrices have same dimensions
    if rows1 != rows2 or cols1 != cols2:
        return None, 0
    
    operations = 0
    result = []
    
    print("\nPerforming Matrix Addition:")
    for i in range(rows1):
        row = []
        for j in range(cols1):
            operations += 1
            sum_val = matrix1[i][j] + matrix2[i][j]
            row.append(sum_val)
            
            # Print the current operation
            print(f"\nAdding elements at position ({i},{j}):")
            print(f"{matrix1[i][j]} + {matrix2[i][j]} = {sum_val}")
            print_matrices_state(matrix1, matrix2, result + [row], i, j)
        
        result.append(row)
    
    return result, operations

def print_matrices_state(matrix1, matrix2, result, current_i, current_j):
    """Print current state of matrices with markers for current operation."""
    def print_matrix_row(matrix, row, current_i, current_j):
        print("[ ", end="")
        for col in range(len(matrix[row])):
            if row == current_i and col == current_j:
                print(f"[{matrix[row][col]:2}]", end=" ")
            else:
                print(f"{matrix[row][col]:3}", end=" ")
        print("]")
    
    # Print matrices side by side
    print("\nMatrix 1      Matrix 2      Result")
    print("-" * 40)
    
    max_rows = max(len(matrix1), len(matrix2), len(result))
    for i in range(max_rows):
        # Print matrix1 row
        if i < len(matrix1):
            print_matrix_row(matrix1, i, current_i, current_j)
        else:
            print(" " * 12, end="")
        
        # Separator
        print("  +  " if i == max_rows//2 else "     ", end="")
        
        # Print matrix2 row
        if i < len(matrix2):
            print_matrix_row(matrix2, i, current_i, current_j)
        else:
            print(" " * 12, end="")
        
        # Separator
        print("  =  " if i == max_rows//2 else "     ", end="")
        
        # Print result row
        if i < len(result):
            print_matrix_row(result, i, current_i, current_j)
        else:
            print()

def get_matrix_input(matrix_num):
    """Get matrix input from user."""
    try:
        rows = int(input(f"\nEnter number of rows for Matrix {matrix_num}: "))
        cols = int(input(f"Enter number of columns for Matrix {matrix_num}: "))
        
        if rows <= 0 or cols <= 0:
            print("Dimensions must be positive!")
            return None
        
        print(f"\nEnter elements for Matrix {matrix_num}:")
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
    """Test matrix addition implementation."""
    # Get input matrices
    matrix1 = get_matrix_input(1)
    if matrix1 is None:
        return
    
    matrix2 = get_matrix_input(2)
    if matrix2 is None:
        return
    
    # Print original matrices
    print("\nMatrix 1:")
    for row in matrix1:
        print(row)
    
    print("\nMatrix 2:")
    for row in matrix2:
        print(row)
    
    # Perform addition and measure time
    import time
    start_time = time.time()
    result, operations = matrix_addition(matrix1, matrix2)
    end_time = time.time()
    
    # Print results
    if result:
        print("\nAddition completed!")
        print(f"Operations performed: {operations}")
        print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
        
        print("\nResultant Matrix:")
        for row in result:
            print(row)
    else:
        print("\nError: Matrices cannot be added (different dimensions)")

if __name__ == "__main__":
    main()
