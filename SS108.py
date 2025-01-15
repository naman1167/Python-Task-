def generate_permutations(arr):
    """
    Generate all permutations of a list using backtracking.
    Time Complexity: O(n!)
    Space Complexity: O(n)
    """
    def backtrack(start):
        nonlocal permutations, steps
        
        if start == len(arr):
            permutations.append(arr[:])
            print("\nFound permutation:", arr)
            print_permutation_state(arr, start, len(permutations))
            return
        
        for i in range(start, len(arr)):
            steps += 1
            # Swap elements to create new permutation
            arr[start], arr[i] = arr[i], arr[start]
            
            print(f"\nStep {steps}: Swapping elements at positions {start} and {i}")
            print_permutation_state(arr, start, len(permutations))
            
            # Recursively generate permutations for remaining elements
            backtrack(start + 1)
            
            # Backtrack by restoring the original order
            arr[start], arr[i] = arr[i], arr[start]
    
    permutations = []
    steps = 0
    
    print("\nGenerating all permutations:")
    print("Initial array:", arr)
    backtrack(0)
    
    return permutations, steps

def print_permutation_state(arr, current_pos, count):
    """Print current state of permutation generation."""
    print("Current array:", end=" ")
    for i in range(len(arr)):
        if i == current_pos:
            print(f"[{arr[i]}]", end=" ")
        else:
            print(arr[i], end=" ")
    print(f"\nPermutations found: {count}")
    
    # Visual progress
    if len(arr) <= 8:  # Only show tree for small arrays
        depth = current_pos + 1
        width = len(arr) - depth
        print("\nBacktracking tree level:")
        print("  " * depth + "*")
        print("  " * depth + "|")
        print("  " * depth + "-" * (width * 2))

def analyze_permutations(permutations, original):
    """Analyze the generated permutations."""
    if not permutations:
        return
    
    print("\nPermutation Analysis:")
    print(f"Total permutations: {len(permutations)}")
    print(f"Expected permutations: {factorial(len(original))}")
    
    # Verify all permutations are unique
    unique_perms = set(tuple(p) for p in permutations)
    print(f"Unique permutations: {len(unique_perms)}")
    
    # Check if all elements appear in each permutation
    all_elements_present = all(sorted(p) == sorted(original) for p in permutations)
    print("All elements present in each permutation:", 
          "Yes" if all_elements_present else "No")
    
    # First few permutations
    print("\nFirst 5 permutations:")
    for i, perm in enumerate(permutations[:5]):
        print(f"{i+1}. {perm}")
    
    if len(permutations) > 5:
        print("...")

def factorial(n):
    """Calculate factorial of n."""
    if n <= 1:
        return 1
    return n * factorial(n-1)

def get_user_input():
    """Get list from user."""
    try:
        input_str = input("Enter space-separated elements: ")
        arr = [int(x) for x in input_str.split()]
        
        if not arr:
            print("List cannot be empty!")
            return None
        
        # Check for duplicates
        if len(arr) != len(set(arr)):
            print("Warning: List contains duplicates!")
            print("Some permutations may appear multiple times.")
        
        if len(arr) > 8:
            print("Warning: Large input size!")
            print(f"This will generate {factorial(len(arr))} permutations!")
            proceed = input("Continue? (y/n): ").lower()
            if proceed != 'y':
                return None
        
        return arr
    
    except ValueError:
        print("Please enter valid integers!")
        return None

def main():
    """Test permutation generation implementation."""
    # Get input
    arr = get_user_input()
    if arr is None:
        return
    
    original = arr.copy()
    print("\nGenerating permutations for:", arr)
    
    # Generate permutations and measure time
    import time
    start_time = time.time()
    permutations, steps = generate_permutations(arr)
    end_time = time.time()
    
    # Print results
    print("\nGeneration completed!")
    print(f"Steps performed: {steps}")
    print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
    
    analyze_permutations(permutations, original)

if __name__ == "__main__":
    main()
