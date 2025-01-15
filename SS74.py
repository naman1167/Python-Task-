def count_lines():
    """Count lines in a text file."""
    try:
        # Get filename
        filename = input("Enter file name: ")
        
        # Check if file exists
        import os
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' does not exist!")
            return
            
        # Count lines
        with open(filename, 'r') as file:
            lines = file.readlines()
            
        # Count different types of lines
        total_lines = len(lines)
        empty_lines = sum(1 for line in lines if line.strip() == '')
        non_empty_lines = total_lines - empty_lines
        
        # Display results
        print(f"\nLine count statistics for '{filename}':")
        print(f"Total lines: {total_lines}")
        print(f"Non-empty lines: {non_empty_lines}")
        print(f"Empty lines: {empty_lines}")
        
        # Additional statistics
        if lines:
            max_length = max(len(line.rstrip()) for line in lines)
            avg_length = sum(len(line.rstrip()) for line in lines) / total_lines
            print(f"\nLongest line length: {max_length} characters")
            print(f"Average line length: {avg_length:.2f} characters")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    count_lines()
