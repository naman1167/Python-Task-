def is_palindrome():
    """Check if a string is a palindrome (case-insensitive)."""
    # Get input string
    text = input("Enter a string to check for palindrome: ")
    
    # Remove spaces and convert to lowercase
    cleaned_text = ''.join(text.lower().split())
    
    # Check if it's a palindrome
    is_pal = cleaned_text == cleaned_text[::-1]
    
    print(f"\nOriginal string: {text}")
    if is_pal:
        print("This is a palindrome!")
    else:
        print("This is not a palindrome.")
        
    # Show the comparison
    print(f"\nAfter removing spaces and converting to lowercase:")
    print(f"Forward:  {cleaned_text}")
    print(f"Reversed: {cleaned_text[::-1]}")

if __name__ == "__main__":
    is_palindrome()
