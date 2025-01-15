def search_word():
    """Search for a word in a file and return line numbers where it appears."""
    try:
        # Get inputs
        filename = input("Enter file name: ")
        word = input("Enter word to search for: ")
        
        # Check if file exists
        import os
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' does not exist!")
            return
            
        # Search for word
        occurrences = []
        with open(filename, 'r') as file:
            for i, line in enumerate(file, 1):
                if word.lower() in line.lower():  # Case-insensitive search
                    occurrences.append((i, line.strip()))
        
        # Display results
        if occurrences:
            print(f"\nFound '{word}' in {len(occurrences)} line(s):")
            for line_num, content in occurrences:
                print(f"\nLine {line_num}:")
                print("-" * 50)
                # Highlight the word in the line
                highlighted = content.replace(word, f"**{word}**")
                print(highlighted)
                print("-" * 50)
        else:
            print(f"\nWord '{word}' not found in the file.")
            
        # Additional statistics
        with open(filename, 'r') as file:
            content = file.read().lower()
            word_count = content.count(word.lower())
            
        print(f"\nWord Statistics:")
        print(f"Total occurrences of '{word}': {word_count}")
        print(f"Found in {len(occurrences)} different lines")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    search_word()
