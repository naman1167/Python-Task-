def find_second_largest():
    """Find the second largest element in a list of unique integers."""
    try:
        numbers = [int(x) for x in input("Enter unique integers separated by spaces: ").split()]
        if len(numbers) < 2:
            print("Please enter at least 2 numbers!")
            return
        
        # Convert to set to remove any duplicates and ensure uniqueness
        unique_numbers = list(set(numbers))
        if len(unique_numbers) < 2:
            print("Please enter at least 2 different numbers!")
            return
            
        # Sort in descending order
        unique_sorted = sorted(unique_numbers, reverse=True)
        print(f"The list: {numbers}")
        print(f"The second largest element is: {unique_sorted[1]}")
        
    except ValueError:
        print("Please enter valid integers!")

if __name__ == "__main__":
    find_second_largest()