def access_tuple():
    """Create a tuple of strings and access elements by index."""
    # Create a tuple of strings
    strings_tuple = ('apple', 'banana', 'orange', 'grape', 'mango')
    
    try:
        print(f"Tuple contents: {strings_tuple}")
        print(f"Tuple length: {len(strings_tuple)}")
        index = int(input(f"Enter an index (0-{len(strings_tuple)-1}): "))
        
        if 0 <= index < len(strings_tuple):
            print(f"Element at index {index}: {strings_tuple[index]}")
        else:
            print(f"Index must be between 0 and {len(strings_tuple)-1}")
            
    except ValueError:
        print("Please enter a valid integer index!")

if __name__ == "__main__":
    access_tuple()
