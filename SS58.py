def capitalize_words():
    """Capitalize the first letter of every word."""
    # Get input string
    text = input("Enter a string: ")
    
    # Method 1: Using title()
    title_case = text.title()
    
    # Method 2: Manual capitalization
    manual_case = ' '.join(word.capitalize() for word in text.split())
    
    # Display results
    print("\nCapitalization Results:")
    print(f"Original:  {text}")
    print(f"Title:     {title_case}")
    
    # Show which words were modified
    original_words = text.split()
    capitalized_words = title_case.split()
    
    print("\nChanges made:")
    for orig, cap in zip(original_words, capitalized_words):
        if orig != cap:
            print(f"'{orig}' → '{cap}'")

if __name__ == "__main__":
    capitalize_words()
