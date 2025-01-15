def reverse_string():
    """Reverse a string input by the user."""
    # Get input string
    text = input("Enter a string to reverse: ")
    
    # Method 1: Using string slicing
    reversed_str1 = text[::-1]
    
    # Method 2: Using reversed() function
    reversed_str2 = ''.join(reversed(text))
    
    print(f"\nOriginal string: {text}")
    print(f"Reversed string: {reversed_str1}")
    print("\nNote: Both methods produce the same result!")

if __name__ == "__main__":
    reverse_string()
