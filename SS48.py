def invert_dictionary():
    """Swap keys and values in a dictionary if values are unique."""
    # Create dictionary from user input
    original_dict = {}
    print("Enter key-value pairs (empty key to finish):")
    while True:
        key = input("Enter key: ")
        if not key:
            break
        value = input("Enter value: ")
        original_dict[key] = value
    
    # Check if values are unique
    values = list(original_dict.values())
    if len(values) != len(set(values)):
        print("\nError: Values are not unique! Cannot invert dictionary.")
        print("Original dictionary:", original_dict)
        return
    
    # Invert dictionary
    inverted_dict = {value: key for key, value in original_dict.items()}
    
    # Display results
    print("\nOriginal dictionary:", original_dict)
    print("Inverted dictionary:", inverted_dict)

if __name__ == "__main__":
    invert_dictionary()
