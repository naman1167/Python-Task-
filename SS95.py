def quick_sort(arr):
    """
    Sort a list using quick sort algorithm.
    Time Complexity: Average O(n log n), Worst O(n^2)
    Space Complexity: O(log n)
    """
    global comparisons, swaps
    comparisons = 0
    swaps = 0
    
    def partition(arr, low, high):
        """
        Partition the array using the last element as pivot.
        Places pivot at its correct position and places all smaller elements
        to left of pivot and all greater elements to right of pivot.
        """
        global comparisons, swaps
        
        pivot = arr[high]
        print(f"\nPartitioning with pivot {pivot}")
        print_array_state(arr, high, -1, low, high)
        
        i = low - 1  # Index of smaller element
        
        for j in range(low, high):
            comparisons += 1
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                i += 1  # Increment index of smaller element
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1
                    print_array_state(arr, j, i, low, high)
        
        # Place pivot in its correct position
        if i + 1 != high:
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            swaps += 1
            print_array_state(arr, i + 1, high, low, high)
        
        return i + 1
    
    def quick_sort_recursive(arr, low, high):
        """Recursive function to sort array using quick sort."""
        if low < high:
            # Partition array and get pivot position
            pivot_pos = partition(arr, low, high)
            
            print(f"\nRecursing on left partition (elements < {arr[pivot_pos]})")
            # Sort elements before pivot
            quick_sort_recursive(arr, low, pivot_pos - 1)
            
            print(f"\nRecursing on right partition (elements > {arr[pivot_pos]})")
            # Sort elements after pivot
            quick_sort_recursive(arr, pivot_pos + 1, high)
    
    # Start the recursive quick sort
    quick_sort_recursive(arr, 0, len(arr) - 1)
    return comparisons, swaps

def print_array_state(arr, current, swap_pos, low, high):
    """Print current state of array with markers for important elements."""
    print("Array state:", end=" ")
    for i in range(len(arr)):
        if i == current:
            print(f"[{arr[i]}]", end=" ")  # Current element
        elif i == swap_pos:
            print(f"({arr[i]})", end=" ")  # Swap position
        elif low <= i <= high:
            print(f"{arr[i]}", end=" ")  # Current partition
        else:
            print(f"*{arr[i]}*", end=" ")  # Outside current partition
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
    """Test quick sort implementation."""
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
    comparisons, swaps = quick_sort(arr_copy)
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
