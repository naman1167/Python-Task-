def linear_search(arr, target):
    """
    Perform linear search to find target in array.
    Returns: (index if found, steps taken)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    steps = 0
    found_indices = []  # Track all occurrences
    
    print("\nStarting Linear Search:")
    
    for i in range(len(arr)):
        steps += 1
        print(f"\nStep {steps}:")
        print_array_state(arr, i, target)
        
        if arr[i] == target:
            print(f"Found {target} at index {i}!")
            found_indices.append(i)
    
    if not found_indices:
        print(f"\nTarget {target} not found in array")
        return -1, steps
    
    return found_indices, steps

def print_array_state(arr, current, target):
    """Print current state of array with search position."""
    print("Array state:", end=" ")
    for i in range(len(arr)):
        if i == current:
            if arr[i] == target:
                print(f"[{arr[i]}]", end=" ")  # Found target
            else:
                print(f"({arr[i]})", end=" ")  # Current element
        else:
            print(arr[i], end=" ")
    print()
    
    # Print current position marker
    print("           ", end=" ")
    for i in range(len(arr)):
        if i == current:
            print("^", end=" ")
        else:
            print(" ", end=" ")
    print()

def get_user_input():
    """Get list and target from user."""
    try:
        input_str = input("Enter space-separated integers: ")
        arr = [int(x) for x in input_str.split()]
        target = int(input("Enter target number to find: "))
        return arr, target
    except ValueError:
        print("Please enter valid integers!")
        return None, None

def main():
    """Test linear search implementation."""
    # Get input from user
    arr, target = get_user_input()
    if arr is None:
        return
    
    if not arr:
        print("List is empty!")
        return
    
    # Print original array
    print("\nSearching in array:", arr)
    print(f"Looking for: {target}")
    
    # Perform linear search and measure time
    import time
    start_time = time.time()
    result, steps = linear_search(arr, target)
    end_time = time.time()
    
    # Print results
    print("\nSearch completed!")
    if result != -1:
        if isinstance(result, list):
            print(f"Found {target} at indices: {result}")
            print(f"Number of occurrences: {len(result)}")
        else:
            print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found in array")
    
    print(f"Steps taken: {steps}")
    print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
    
    # Compare with built-in methods
    print("\nVerification using built-in methods:")
    try:
        index = arr.index(target)
        print(f"First occurrence at index: {index}")
        count = arr.count(target)
        print(f"Total occurrences: {count}")
    except ValueError:
        print("Target not found (verified)")

if __name__ == "__main__":
    main()
