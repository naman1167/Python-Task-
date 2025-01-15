def selection_sort(arr):
    """
    Sort a list using selection sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    comparisons = 0  # Count comparisons
    swaps = 0       # Count swaps
    n = len(arr)
    
    for i in range(n):
        # Find minimum element in unsorted part
        min_idx = i
        print(f"\nPass {i+1}: Finding minimum from index {i} to {n-1}")
        print_array_state(arr, i, min_idx)
        
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
                print_array_state(arr, i, min_idx)
        
        # Swap minimum element with first element of unsorted part
        if min_idx != i:
            print(f"\nSwapping {arr[i]} with {arr[min_idx]}")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
            print_array_state(arr, i, min_idx)
    
    return comparisons, swaps

def print_array_state(arr, current, min_idx):
    """Print current state of array with markers for important elements."""
    print("Array state:", end=" ")
    for i in range(len(arr)):
        if i == current:
            print(f"[{arr[i]}]", end=" ")  # Current position
        elif i == min_idx:
            print(f"({arr[i]})", end=" ")  # Current minimum
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
    """Test selection sort implementation."""
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
    comparisons, swaps = selection_sort(arr_copy)
    end_time = time.time()
    
    # Print results
    print("\nSorting completed!")
    print(f"Comparisons made: {comparisons}")
    print(f"Swaps performed: {swaps}")
    print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
    print("Sorted array:", arr_copy)
    
    # Verify if array is sorted
    is_sorted = all(arr_copy[i] <= arr_copy[i+1] for i in range(len(arr_copy)-1))
    print("Verification:", "Sorted correctly!" if is_sorted else "Something went wrong!")

if __name__ == "__main__":
    main()
