def insertion_sort(arr):
    """
    Sort a list using insertion sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    steps = 0  # Count comparisons
    shifts = 0  # Count shifts
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Visualize before insertion
        print(f"\nInserting {key}:")
        print_array_state(arr, i, j)
        
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            steps += 1
            arr[j + 1] = arr[j]
            shifts += 1
            j -= 1
            # Visualize during insertion
            print_array_state(arr, j+1, j)
        
        arr[j + 1] = key
        shifts += 1
        
        # Visualize after insertion
        print("\nAfter insertion:")
        print_array_state(arr, j+1, -1)
    
    return steps, shifts

def print_array_state(arr, current, comparing):
    """Print current state of array with markers for key elements."""
    print("Array state:", end=" ")
    for i in range(len(arr)):
        if i == current:
            print(f"[{arr[i]}]", end=" ")  # Current element
        elif i == comparing:
            print(f"({arr[i]})", end=" ")  # Comparing element
        else:
            print(arr[i], end=" ")
    print()

def get_user_input():
    """Get list of integers from user."""
    try:
        input_str = input("Enter space-separated integers to sort: ")
        return [int(x) for x in input_str.split()]
    except ValueError:
        print("Please enter valid integers!")
        return None

def main():
    """Test insertion sort implementation."""
    # Get input from user
    arr = get_user_input()
    if arr is None:
        return
    
    if not arr:
        print("List is empty!")
        return
    
    # Print original array
    print("\nOriginal array:", arr)
    
    # Create a copy for sorting
    arr_copy = arr.copy()
    
    # Sort and measure time
    import time
    start_time = time.time()
    steps, shifts = insertion_sort(arr_copy)
    end_time = time.time()
    
    # Print results
    print("\nSorting completed!")
    print(f"Comparisons made: {steps}")
    print(f"Shifts performed: {shifts}")
    print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
    print("Sorted array:", arr_copy)
    
    # Verify if array is sorted
    is_sorted = all(arr_copy[i] <= arr_copy[i+1] for i in range(len(arr_copy)-1))
    print("Verification:", "Sorted correctly!" if is_sorted else "Something went wrong!")

if __name__ == "__main__":
    main()
