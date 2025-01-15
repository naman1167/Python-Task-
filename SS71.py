def write_to_file():
    """Write user input to a text file."""
    try:
        # Get input from user
        text = input("Enter text to write to file: ")
        
        # Write to file
        with open('output.txt', 'w') as file:
            file.write(text)
            
        print("\nSuccessfully wrote to output.txt!")
        
        # Show file details
        import os
        if os.path.exists('output.txt'):
            size = os.path.getsize('output.txt')
            print(f"\nFile Statistics:")
            print(f"Characters written: {len(text)}")
            print(f"File size: {size} bytes")
            print(f"File location: {os.path.abspath('output.txt')}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    write_to_file()
