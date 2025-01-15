def set_operations():
    """Perform set operations on two lists."""
    try:
        # Get input lists
        list1 = input("Enter first list elements separated by spaces: ").split()
        list2 = input("Enter second list elements separated by spaces: ").split()
        
        # Convert to sets
        set1 = set(list1)
        set2 = set(list2)
        
        # Perform set operations
        print("\nSet 1:", set1)
        print("Set 2:", set2)
        print("\nSet Operations:")
        print("Union:", set1.union(set2))
        print("Intersection:", set1.intersection(set2))
        print("Difference (Set1 - Set2):", set1.difference(set2))
        print("Difference (Set2 - Set1):", set2.difference(set1))
        print("Symmetric Difference:", set1.symmetric_difference(set2))
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    set_operations()
