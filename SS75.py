def count_words():
    """Count words in a text file."""
    try:
        # Get filename
        filename = input("Enter file name: ")
        
        # Check if file exists
        import os
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' does not exist!")
            return
            
        # Read and count words
        with open(filename, 'r') as file:
            content = file.read()
            
        # Split into words and clean them
        words = [word.strip('.,!?()[]{}":;') for word in content.split()]
        words = [word for word in words if word]  # Remove empty strings
        
        # Count word frequencies
        from collections import Counter
        word_freq = Counter(words)
        
        # Display results
        print(f"\nWord count statistics for '{filename}':")
        print(f"Total words: {len(words)}")
        print(f"Unique words: {len(word_freq)}")
        
        # Show most common words
        if word_freq:
            print("\nMost common words:")
            for word, count in word_freq.most_common(5):
                print(f"'{word}': {count} time(s)")
                
        # Additional statistics
        if words:
            max_length = max(len(word) for word in words)
            avg_length = sum(len(word) for word in words) / len(words)
            print(f"\nLongest word length: {max_length} characters")
            print(f"Average word length: {avg_length:.2f} characters")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    count_words()
