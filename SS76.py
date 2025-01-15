def find_longest_line():
    """Find and display the longest line in a text file."""
    try:
        # Get filename
        filename = input("Enter file name: ")
        
        # Check if file exists
        import os
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' does not exist!")
            return
            
        # Read lines and find longest
        with open(filename, 'r') as file:
            lines = file.readlines()
            
        if not lines:
            print("File is empty!")
            return
            
        # Find longest line(s)
        max_length = max(len(line.rstrip()) for line in lines)
        longest_lines = [(i+1, line.rstrip()) for i, line in enumerate(lines) 
                        if len(line.rstrip()) == max_length]
        
        # Display results
        print(f"\nLongest line(s) in '{filename}':")
        print(f"Length: {max_length} characters")
        print("\nLine number(s) and content:")
        for line_num, content in longest_lines:
            print(f"\nLine {line_num}:")
            print("-" * 50)
            print(content)
            print("-" * 50)
        
        # Additional statistics
        total_lines = len(lines)
        avg_length = sum(len(line.rstrip()) for line in lines) / total_lines
        print(f"\nFile Statistics:")
        print(f"Total lines: {total_lines}")
        print(f"Average line length: {avg_length:.2f} characters")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    find_longest_line()
