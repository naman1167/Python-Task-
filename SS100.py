def matrix_multiplication(matrix1, matrix2):
    """
    Multiply two matrices if their dimensions are compatible.
    Returns the resulting matrix and number of operations performed.
    """
    if not (matrix1 and matrix2 and matrix1[0] and matrix2[0]):
        return None, 0
    
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])
    
    # Check if matrices can be multiplied
    if cols1 != rows2:
        return None, 0
    
    operations = 0
    result = []
    
    print("\nPerforming Matrix Multiplication:")
    for i in range(rows1):
        row = []
        for j in range(cols2):
            # Calculate element at position (i,j)
            print(f"\nCalculating element at position ({i},{j}):")
            element = 0
            for k in range(cols1):
                operations += 1
                product = matrix1[i][k] * matrix2[k][j]
                element += product
                
                # Print current multiplication step
                print(f"Step {k+1}: {matrix1[i][k]} × {matrix2[k][j]} = {product}")
                print_matrices_state(matrix1, matrix2, result + [row + [element]], i, j, k)
            
            row.append(element)
            print(f"Final sum for position ({i},{j}): {element}")
        
        result.append(row)
    
    return result, operations

def print_matrices_state(matrix1, matrix2, result, current_i, current_j, current_k=None):
    """Print current state of matrices with markers for current operation."""
    def print_matrix_row(matrix, row, current_i, current_j, current_k=None, is_first=True):
        print("[ ", end="")
        for col in range(len(matrix[row])):
            if is_first and row == current_i and col == current_k:
                print(f"[{matrix[row][col]:2}]", end=" ")
            elif not is_first and row == current_k and col == current_j:
                print(f"[{matrix[row][col]:2}]", end=" ")
            elif (is_first and row == current_i) or (not is_first and col == current_j):
                print(f"({matrix[row][col]:2})", end=" ")
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
            print_matrix_row(matrix1, i, current_i, current_j, current_k, True)
        else:
            print(" " * 12, end="")
        
        # Separator
        print("  ×  " if i == max_rows//2 else "     ", end="")
        
        # Print matrix2 row
        if i < len(matrix2):
            print_matrix_row(matrix2, i, current_i, current_j, current_k, False)
        else:
            print(" " * 12, end="")
        
        # Separator
        print("  =  " if i == max_rows//2 else "     ", end="")
        
        # Print result row
        if i < len(result):
            print_matrix_row(result, i, current_i, current_j, None, True)
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
    """Test matrix multiplication implementation."""
    # Get input matrices
    print("For matrix multiplication (A × B):")
    print("Number of columns in A must equal number of rows in B")
    
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
    
    # Perform multiplication and measure time
    import time
    start_time = time.time()
    result, operations = matrix_multiplication(matrix1, matrix2)
    end_time = time.time()
    
    # Print results
    if result:
        print("\nMultiplication completed!")
        print(f"Operations performed: {operations}")
        print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
        
        print("\nResultant Matrix:")
        for row in result:
            print(row)
    else:
        print("\nError: Matrices cannot be multiplied (incompatible dimensions)")
        print("For matrix multiplication (A × B):")
        print("Number of columns in A must equal number of rows in B")

if __name__ == "__main__":
    main()
