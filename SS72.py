def read_from_file():
    """Read and display content from output.txt."""
    try:
        # Check if file exists
        import os
        if not os.path.exists('output.txt'):
            print("output.txt does not exist! Please run SS71.py first to create it.")
            return
            
        # Read from file
        with open('output.txt', 'r') as file:
            content = file.read()
            
        # Display content
        print("\nFile content:")
        print("-" * 50)
        print(content)
        print("-" * 50)
        
        # Show file statistics
        size = os.path.getsize('output.txt')
        print(f"\nFile Statistics:")
        print(f"Characters: {len(content)}")
        print(f"Words: {len(content.split())}")
        print(f"Lines: {len(content.splitlines())}")
        print(f"File size: {size} bytes")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    read_from_file()
