import string

def count_special_chars():
    """Count special characters in a string."""
    # Get input string
    text = input("Enter a string: ")
    
    # Define character sets
    punctuation = string.punctuation
    special_chars = {char: text.count(char) for char in punctuation if char in text}
    
    # Count results
    total_special = sum(special_chars.values())
    
    # Display results
    print("\nSpecial Character Analysis:")
    if special_chars:
        print("Found special characters:")
        for char, count in special_chars.items():
            print(f"'{char}': {count} time(s)")
    else:
        print("No special characters found!")
    
    print(f"\nTotal special characters: {total_special}")
    
    # Additional statistics
    print("\nCharacter Breakdown:")
    print(f"Letters: {sum(c.isalpha() for c in text)}")
    print(f"Digits: {sum(c.isdigit() for c in text)}")
    print(f"Spaces: {sum(c.isspace() for c in text)}")
    print(f"Special: {total_special}")

if __name__ == "__main__":
    count_special_chars()
