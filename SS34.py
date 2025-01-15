def calculate_sum_average():
    """Calculate sum and average of user input numbers."""
    try:
        numbers = [float(x) for x in input("Enter numbers separated by spaces: ").split()]
        if not numbers:
            return 0, 0
        total = sum(numbers)
        average = total / len(numbers)
        print(f"Sum: {total}")
        print(f"Average: {average}")
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    calculate_sum_average()
