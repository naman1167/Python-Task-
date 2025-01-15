def character_frequency():
    """Count frequency of each character in a string."""
    # Get input string
    text = input("Enter a string: ")
    
    # Create frequency dictionary
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    
    # Display results
    print("\nCharacter Frequency Analysis:")
    
    # Sort by frequency (most common first)
    sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    # Display in columns
    print("\nDetailed Breakdown:")
    print("Char | Count | Visualization")
    print("-" * 40)
    
    for char, count in sorted_chars:
        if char.isspace():
            char_display = "SPACE"
        else:
            char_display = char
        # Create a simple bar chart
        bar = "*" * count
        print(f"'{char_display:5}' | {count:5} | {bar}")
    
    # Additional statistics
    print("\nSummary:")
    print(f"Total characters: {len(text)}")
    print(f"Unique characters: {len(freq)}")
    if sorted_chars:
        most_common = sorted_chars[0]
        print(f"Most frequent: '{most_common[0]}' ({most_common[1]} times)")

if __name__ == "__main__":
    character_frequency()
