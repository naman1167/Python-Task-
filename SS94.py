def merge_sort(arr):
    """
    Sort a list using merge sort algorithm.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    global comparisons, merges
    comparisons = 0
    merges = 0
    
    def merge(arr, left, mid, right):
        """Merge two sorted subarrays."""
        global comparisons, merges
        
        # Create temporary arrays
        L = arr[left:mid+1]
        R = arr[mid+1:right+1]
        
        print(f"\nMerging subarrays: {L} and {R}")
        
        i = j = 0        # Initial indexes for L and R
        k = left         # Initial index for merged array
        
        # Merge the temp arrays back into arr[left..right]
        while i < len(L) and j < len(R):
            comparisons += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            merges += 1
            print_array_state(arr, k-1, left, right)
        
        # Copy remaining elements of L[] if any
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            merges += 1
            print_array_state(arr, k-1, left, right)
        
        # Copy remaining elements of R[] if any
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            merges += 1
            print_array_state(arr, k-1, left, right)
    
    def merge_sort_recursive(arr, left, right):
        """Recursive function to sort array using merge sort."""
        if left < right:
            # Find middle point
            mid = (left + right) // 2
            
            print(f"\nDividing array at index {mid}:")
            print_array_state(arr, mid, left, right)
            
            # Sort first and second halves
            merge_sort_recursive(arr, left, mid)
            merge_sort_recursive(arr, mid + 1, right)
            
            # Merge the sorted halves
            merge(arr, left, mid, right)
    
    # Start the recursive merge sort
    merge_sort_recursive(arr, 0, len(arr)-1)
    return comparisons, merges

def print_array_state(arr, current, left, right):
    """Print current state of array with markers for important elements."""
    print("Array state:", end=" ")
    for i in range(len(arr)):
        if i == current:
            print(f"[{arr[i]}]", end=" ")  # Current element being placed
        elif left <= i <= right:
            print(f"({arr[i]})", end=" ")  # Elements in current subarray
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
    """Test merge sort implementation."""
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
    comparisons, merges = merge_sort(arr_copy)
    end_time = time.time()
    
    # Print results
    print("\nSorting completed!")
    print(f"Comparisons made: {comparisons}")
    print(f"Merges performed: {merges}")
    print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
    print("Sorted array:", arr_copy)
    
    # Verify if array is sorted
    is_sorted = all(arr_copy[i] <= arr_copy[i+1] for i in range(len(arr_copy)-1))
    print("Verification:", "Sorted correctly!" if is_sorted else "Something went wrong!")

if __name__ == "__main__":
    main()
