import random

def knuth_shuffle(arr):
    """
    Implement Fisher-Yates (Knuth) shuffle algorithm.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr)
    swaps = 0
    
    print("\nStarting Knuth Shuffle:")
    print_array_state(arr, -1, -1)
    
    # Start from the last element and swap with random previous element
    for i in range(n-1, 0, -1):
        # Pick a random index from 0 to i
        j = random.randint(0, i)
        
        print(f"\nStep {n-i}/{n-1}:")
        print(f"Swapping elements at indices {i} and {j}")
        
        # Swap arr[i] with the element at random index
        if i != j:
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1
        
        print_array_state(arr, i, j)
    
    return swaps

def print_array_state(arr, pos1, pos2):
    """Print current state of array with markers for swapped elements."""
    print("Array state:", end=" ")
    for i in range(len(arr)):
        if i == pos1:
            print(f"[{arr[i]}]", end=" ")  # First swap position
        elif i == pos2:
            print(f"({arr[i]})", end=" ")  # Second swap position
        else:
            print(arr[i], end=" ")
    print()

def verify_shuffle(original, shuffled):
    """
    Verify that the shuffle is valid:
    1. Same length
    2. Same elements (frequency should match)
    3. Not in the same order (unless length <= 1)
    """
    if len(original) != len(shuffled):
        return False, "Different lengths"
    
    if sorted(original) != sorted(shuffled):
        return False, "Different elements"
    
    if len(original) > 1 and original == shuffled:
        return False, "Same order (not shuffled)"
    
    return True, "Valid shuffle"

def get_user_input():
    """Get list from user."""
    try:
        input_str = input("Enter space-separated elements to shuffle: ")
        return [int(x) for x in input_str.split()]
    except ValueError:
        print("Please enter valid integers!")
        return None

def main():
    """Test Knuth shuffle implementation."""
    # Get input from user
    arr = get_user_input()
    if arr is None:
        return
    
    if not arr:
        print("List is empty!")
        return
    
    # Store original array for verification
    original = arr.copy()
    print("\nOriginal array:", original)
    
    # Set random seed for reproducibility (in practice, you might want to remove this)
    random.seed(42)
    
    # Perform shuffle and measure time
    import time
    start_time = time.time()
    swaps = knuth_shuffle(arr)
    end_time = time.time()
    
    # Print results
    print("\nShuffle completed!")
    print(f"Swaps performed: {swaps}")
    print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
    print("Shuffled array:", arr)
    
    # Verify shuffle
    is_valid, message = verify_shuffle(original, arr)
    print("\nShuffle verification:", message)
    
    # Additional statistics
    if len(arr) > 1:
        unchanged = sum(1 for i in range(len(arr)) if arr[i] == original[i])
        print(f"Elements in original position: {unchanged}/{len(arr)}")
        print(f"Percentage changed: {((len(arr)-unchanged)/len(arr))*100:.1f}%")

if __name__ == "__main__":
    main()
