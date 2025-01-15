def check_element():
    """Check if an element exists in a tuple."""
    # Create a sample tuple
    sample_tuple = ('python', 'java', 'javascript', 'c++', 'ruby')
    
    print(f"Tuple contents: {sample_tuple}")
    element = input("Enter element to search for: ")
    
    if element in sample_tuple:
        index = sample_tuple.index(element)
        print(f"'{element}' found at index {index}")
    else:
        print(f"'{element}' not found in the tuple")

if __name__ == "__main__":
    check_element()
