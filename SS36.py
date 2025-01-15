def remove_duplicates():
    """Remove duplicates from user input list while preserving order."""
    try:
        numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
        unique_list = list(dict.fromkeys(numbers))  # Preserves order in Python 3.7+
        print(f"Original list: {numbers}")
        print(f"List with duplicates removed: {unique_list}")
    except ValueError:
        print("Please enter valid integers!")

if __name__ == "__main__":
    remove_duplicates()
