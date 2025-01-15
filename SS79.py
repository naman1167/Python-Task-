def remove_blank_lines():
    """Remove blank lines from a file."""
    try:
        # Get filenames
        source = input("Enter source file name: ")
        target = input("Enter target file name: ")
        
        # Check if source file exists
        import os
        if not os.path.exists(source):
            print(f"Error: Source file '{source}' does not exist!")
            return
            
        # Check if target file already exists
        if os.path.exists(target):
            confirm = input(f"'{target}' already exists. Overwrite? (y/n): ")
            if confirm.lower() != 'y':
                print("Operation cancelled.")
                return
        
        # Read source file and remove blank lines
        with open(source, 'r') as src:
            lines = src.readlines()
            
        # Count original statistics
        total_lines = len(lines)
        blank_lines = sum(1 for line in lines if line.strip() == '')
        
        # Remove blank lines and write to target
        non_blank_lines = [line for line in lines if line.strip()]
        with open(target, 'w') as dst:
            dst.writelines(non_blank_lines)
            
        # Display results
        print(f"\nProcessing complete!")
        print(f"\nStatistics:")
        print(f"Original file lines: {total_lines}")
        print(f"Blank lines removed: {blank_lines}")
        print(f"Lines in new file: {len(non_blank_lines)}")
        
        # Show file sizes
        src_size = os.path.getsize(source)
        dst_size = os.path.getsize(target)
        print(f"\nFile sizes:")
        print(f"Source file: {src_size} bytes")
        print(f"Target file: {dst_size} bytes")
        print(f"Size reduction: {src_size - dst_size} bytes")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    remove_blank_lines()
