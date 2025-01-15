def bubble_sort(arr):
    """
    Sort a list using bubble sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    steps = 0  # Count number of steps
    swaps = 0  # Count number of swaps
    
    for i in range(n):
        # Flag to optimize for already sorted array
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            steps += 1
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                swaps += 1
            
            # Visualize current state
            print_array_state(arr, j, j+1)
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return steps, swaps

def print_array_state(arr, pos1, pos2):
    """Print current state of array with markers for compared elements."""
    print("\nCurrent state:", end=" ")
    for i in range(len(arr)):
        if i == pos1:
            print(f"[{arr[i]}]", end=" ")
        elif i == pos2:
            print(f"({arr[i]})", end=" ")
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
    """Test bubble sort implementation."""
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
    steps, swaps = bubble_sort(arr_copy)
    end_time = time.time()
    
    # Print results
    print("\nSorting completed!")
    print(f"Steps taken: {steps}")
    print(f"Swaps made: {swaps}")
    print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
    print("Sorted array:", arr_copy)
    
    # Verify if array is sorted
    is_sorted = all(arr_copy[i] <= arr_copy[i+1] for i in range(len(arr_copy)-1))
    print("Verification:", "Sorted correctly!" if is_sorted else "Something went wrong!")

if __name__ == "__main__":
    main()
