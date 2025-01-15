def modify_tuple():
    """Convert tuple to list, modify it, and convert back to tuple."""
    try:
        # Get input as tuple
        elements = tuple(input("Enter elements separated by spaces: ").split())
        print(f"Original tuple: {elements}")
        
        # Convert to list
        elements_list = list(elements)
        print(f"Converted to list: {elements_list}")
        
        # Modify list
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        
        if 0 <= index < len(elements_list):
            elements_list[index] = new_value
            print(f"Modified list: {elements_list}")
            
            # Convert back to tuple
            modified_tuple = tuple(elements_list)
            print(f"Converted back to tuple: {modified_tuple}")
        else:
            print(f"Index must be between 0 and {len(elements_list)-1}")
            
    except ValueError:
        print("Please enter a valid index!")

if __name__ == "__main__":
    modify_tuple()
