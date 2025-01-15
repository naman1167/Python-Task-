def count_words():
    """Count frequency of words in a string."""
    # Get input string
    text = input("Enter a string: ")
    
    # Split into words and create dictionary
    words = text.lower().split()
    word_count = {}
    
    # Count word frequencies
    for word in words:
        # Remove punctuation from word edges
        word = word.strip('.,!?()[]{}":;')
        if word:  # if word is not empty after stripping
            word_count[word] = word_count.get(word, 0) + 1
    
    # Display results
    print("\nWord frequencies:")
    for word, count in sorted(word_count.items()):
        print(f"'{word}': {count}")

if __name__ == "__main__":
    count_words()
