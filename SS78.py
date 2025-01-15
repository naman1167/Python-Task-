def append_to_file():
    """Append text to a file without overwriting existing content."""
    try:
        # Check if file exists
        import os
        if not os.path.exists('output.txt'):
            print("Note: output.txt doesn't exist. It will be created.")
            
        # Get input from user
        text = input("Enter text to append: ")
        
        # Read existing content first
        existing_content = ""
        if os.path.exists('output.txt'):
            with open('output.txt', 'r') as file:
                existing_content = file.read()
        
        # Append to file
        with open('output.txt', 'a') as file:
            # Add newline if file is not empty and doesn't end with one
            if existing_content and not existing_content.endswith('\n'):
                file.write('\n')
            file.write(text)
            
        print("\nSuccessfully appended to output.txt!")
        
        # Show file statistics
        with open('output.txt', 'r') as file:
            new_content = file.read()
            
        print(f"\nFile Statistics:")
        print(f"Previous size: {len(existing_content)} characters")
        print(f"Appended text: {len(text)} characters")
        print(f"Current size: {len(new_content)} characters")
        print(f"File location: {os.path.abspath('output.txt')}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    append_to_file()
