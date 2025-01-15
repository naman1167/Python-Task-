def sum_of_digits():
    """Compute sum of digits of an integer using a loop."""
    try:
        num = input("Enter a number: ")
        
        # Method 1: Using loop
        total1 = 0
        for digit in num:
            if digit.isdigit():
                total1 += int(digit)
                
        # Method 2: Using sum() function
        total2 = sum(int(digit) for digit in num if digit.isdigit())
        
        # Display results
        print(f"\nNumber: {num}")
        print("Calculation:", " + ".join(digit for digit in num if digit.isdigit()))
        print(f"Sum of digits: {total1}")
        
        # Additional statistics
        digits = [int(d) for d in num if d.isdigit()]
        if digits:
            print(f"\nNumber of digits: {len(digits)}")
            print(f"Average of digits: {sum(digits)/len(digits):.2f}")
            print(f"Maximum digit: {max(digits)}")
            print(f"Minimum digit: {min(digits)}")
        
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    sum_of_digits()
