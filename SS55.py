def remove_spaces():
    """Remove all spaces from a string."""
    # Get input string
    text = input("Enter a string: ")
    
    # Remove spaces using different methods
    # Method 1: replace()
    no_spaces1 = text.replace(" ", "")
    
    # Method 2: join()
    no_spaces2 = "".join(text.split())
    
    # Display results
    print(f"\nOriginal string: '{text}'")
    print(f"Without spaces:  '{no_spaces1}'")
    print(f"\nNumber of spaces removed: {text.count(' ')}")
    
    # Verify both methods produce same result
    assert no_spaces1 == no_spaces2, "Methods produced different results!"

if __name__ == "__main__":
    remove_spaces()
