def convert_case():
    """Convert string to different cases."""
    # Get input string
    text = input("Enter a string: ")
    
    # Convert to different cases
    upper_case = text.upper()
    lower_case = text.lower()
    title_case = text.title()
    
    # Display results
    print("\nCase Conversions:")
    print(f"Original:    {text}")
    print(f"Upper case:  {upper_case}")
    print(f"Lower case:  {lower_case}")
    print(f"Title case:  {title_case}")
    
    # Additional information
    print("\nCharacter Analysis:")
    print(f"Uppercase letters: {sum(1 for c in text if c.isupper())}")
    print(f"Lowercase letters: {sum(1 for c in text if c.islower())}")
    print(f"Other characters: {sum(1 for c in text if not c.isalpha())}")

if __name__ == "__main__":
    convert_case()
