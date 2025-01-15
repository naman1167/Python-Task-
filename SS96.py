def binary_search(arr, target):
    """
    Perform binary search to find target in sorted array.
    Returns: (index if found, steps taken, comparisons made)
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if not arr:
        return -1, 0, 0
    
    left, right = 0, len(arr) - 1
    steps = 0
    comparisons = 0
    
    print("\nStarting Binary Search:")
    print_array_state(arr, -1, left, right, target)
    
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        print(f"\nStep {steps}:")
        print(f"Checking middle element at index {mid}")
        print_array_state(arr, mid, left, right, target)
        
        # First comparison
        comparisons += 1
        if arr[mid] == target:
            print(f"Found {target} at index {mid}!")
            return mid, steps, comparisons
        
        # Second comparison
        comparisons += 1
        if arr[mid] < target:
            print(f"{arr[mid]} < {target}, searching right half")
            left = mid + 1
        else:
            print(f"{arr[mid]} > {target}, searching left half")
            right = mid - 1
        
        print_array_state(arr, -1, left, right, target)
    
    print(f"\nTarget {target} not found in array")
    return -1, steps, comparisons

def print_array_state(arr, mid, left, right, target):
    """Print current state of array with search boundaries."""
    print("Array state:", end=" ")
    for i in range(len(arr)):
        if i == mid:
            print(f"[{arr[i]}]", end=" ")  # Current middle element
        elif left <= i <= right:
            print(f"{arr[i]}", end=" ")    # Current search range
        else:
            print(f"*{arr[i]}*", end=" ")  # Outside search range
    print()
    
    # Print search range markers
    print("           ", end=" ")
    for i in range(len(arr)):
        if i == left and i == right:
            print("^", end=" ")
        elif i == left:
            print("L", end=" ")
        elif i == right:
            print("R", end=" ")
        else:
            print(" ", end=" ")
    print()

def get_user_input():
    """Get sorted list and target from user."""
    try:
        input_str = input("Enter space-separated sorted integers: ")
        arr = [int(x) for x in input_str.split()]
        
        # Verify if array is sorted
        if not all(arr[i] <= arr[i+1] for i in range(len(arr)-1)):
            print("Warning: Input array is not sorted!")
            arr.sort()
            print("Sorted array:", arr)
        
        target = int(input("Enter target number to find: "))
        return arr, target
    except ValueError:
        print("Please enter valid integers!")
        return None, None

def main():
    """Test binary search implementation."""
    # Get input from user
    arr, target = get_user_input()
    if arr is None:
        return
    
    # Print original array
    print("\nSearching in array:", arr)
    print(f"Looking for: {target}")
    
    # Perform binary search and measure time
    import time
    start_time = time.time()
    index, steps, comparisons = binary_search(arr, target)
    end_time = time.time()
    
    # Print results
    print("\nSearch completed!")
    if index != -1:
        print(f"Found {target} at index {index}")
    else:
        print(f"{target} not found in array")
    
    print(f"Steps taken: {steps}")
    print(f"Comparisons made: {comparisons}")
    print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")

if __name__ == "__main__":
    main()
