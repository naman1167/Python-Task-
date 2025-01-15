def copy_file():
    """Copy contents from one file to another."""
    try:
        # Get file names
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
        
        # Copy file
        with open(source, 'r') as src, open(target, 'w') as dst:
            content = src.read()
            dst.write(content)
            
        # Show statistics
        src_size = os.path.getsize(source)
        dst_size = os.path.getsize(target)
        
        print(f"\nFile successfully copied!")
        print(f"\nStatistics:")
        print(f"Source file size: {src_size} bytes")
        print(f"Target file size: {dst_size} bytes")
        print(f"Characters copied: {len(content)}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    copy_file()
