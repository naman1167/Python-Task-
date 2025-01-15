def merge_dictionaries():
    """Merge two dictionaries into a new one."""
    # Create first dictionary
    dict1 = {}
    print("Enter key-value pairs for first dictionary (empty key to finish):")
    while True:
        key = input("Enter key: ")
        if not key:
            break
        value = input("Enter value: ")
        dict1[key] = value
    
    # Create second dictionary
    dict2 = {}
    print("\nEnter key-value pairs for second dictionary (empty key to finish):")
    while True:
        key = input("Enter key: ")
        if not key:
            break
        value = input("Enter value: ")
        dict2[key] = value
    
    # Merge dictionaries
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    
    # Display results
    print("\nDictionary 1:", dict1)
    print("Dictionary 2:", dict2)
    print("Merged dictionary:", merged_dict)

if __name__ == "__main__":
    merge_dictionaries()

