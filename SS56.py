def find_longest_word():
    """Find the longest word in a sentence."""
    # Get input sentence
    sentence = input("Enter a sentence: ")
    
    # Split into words and remove punctuation
    words = [word.strip('.,!?()[]{}":;') for word in sentence.split()]
    
    if not words:
        print("No words found in the input.")
        return
    
    # Find longest word(s)
    max_length = len(max(words, key=len))
    longest_words = [word for word in words if len(word) == max_length]
    
    # Display results
    print(f"\nAll words: {words}")
    print(f"\nLongest word(s) ({max_length} characters):")
    for word in longest_words:
        print(f"- {word}")
    
    # Additional statistics
    print(f"\nWord count: {len(words)}")
    print(f"Average word length: {sum(len(word) for word in words) / len(words):.2f}")

if __name__ == "__main__":
    find_longest_word()
