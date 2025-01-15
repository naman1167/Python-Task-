def file_statistics():
    """Display comprehensive file statistics."""
    try:
        # Get filename
        filename = input("Enter file name: ")
        
        # Check if file exists
        import os
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' does not exist!")
            return
            
        # Read file content
        with open(filename, 'r') as file:
            content = file.read()
            file.seek(0)  # Reset file pointer
            lines = file.readlines()
            
        # Calculate various statistics
        char_count = len(content)
        word_count = len(content.split())
        line_count = len(lines)
        blank_lines = sum(1 for line in lines if line.strip() == '')
        non_blank_lines = line_count - blank_lines
        
        # Count different types of characters
        letters = sum(c.isalpha() for c in content)
        digits = sum(c.isdigit() for c in content)
        spaces = sum(c.isspace() for c in content)
        punctuation = sum(not c.isalnum() and not c.isspace() for c in content)
        
        # Word analysis
        words = [word.strip('.,!?()[]{}":;') for word in content.split()]
        words = [word for word in words if word]  # Remove empty strings
        from collections import Counter
        word_freq = Counter(words)
        
        # Display results
        print(f"\nFile Statistics for '{filename}':")
        print("-" * 50)
        
        print("\nBasic Information:")
        print(f"File size: {os.path.getsize(filename)} bytes")
        print(f"Last modified: {os.path.getmtime(filename)}")
        
        print("\nLine Statistics:")
        print(f"Total lines: {line_count}")
        print(f"Non-blank lines: {non_blank_lines}")
        print(f"Blank lines: {blank_lines}")
        
        print("\nCharacter Statistics:")
        print(f"Total characters: {char_count}")
        print(f"Letters: {letters}")
        print(f"Digits: {digits}")
        print(f"Spaces: {spaces}")
        print(f"Punctuation marks: {punctuation}")
        
        print("\nWord Statistics:")
        print(f"Total words: {word_count}")
        print(f"Unique words: {len(word_freq)}")
        
        if word_freq:
            print("\nMost common words:")
            for word, count in word_freq.most_common(5):
                print(f"'{word}': {count} time(s)")
        
        # Calculate averages
        if non_blank_lines > 0:
            avg_line_length = sum(len(line.rstrip()) for line in lines) / non_blank_lines
            print(f"\nAverage line length: {avg_line_length:.2f} characters")
            
        if words:
            avg_word_length = sum(len(word) for word in words) / len(words)
            print(f"Average word length: {avg_word_length:.2f} characters")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_statistics()
