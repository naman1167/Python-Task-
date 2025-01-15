def count_numbers_type(numbers):
    """Count positive, negative, and zero numbers in a list."""
    positive = sum(1 for num in numbers if num > 0)
    negative = sum(1 for num in numbers if num < 0)
    zero = sum(1 for num in numbers if num == 0)
    return positive, negative, zero

def main():
    try:
        numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
        pos, neg, zeros = count_numbers_type(numbers)
        print(f"Positive numbers: {pos}")
        print(f"Negative numbers: {neg}")
        print(f"Zeros: {zeros}")
    except ValueError:
        print("Please enter valid integers!")

if __name__ == "__main__":
    main()
