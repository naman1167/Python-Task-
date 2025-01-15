def factorial(n):
    """Calculate factorial of a number."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def is_strong_number(num):
    """Check if a number is a strong number."""
    # Calculate sum of factorials of digits
    digit_fact_sum = sum(factorial(int(digit)) for digit in str(num))
    return digit_fact_sum == num

def check_strong_number():
    """Main function to check strong numbers."""
    try:
        num = int(input("Enter a number to check if it's a strong number: "))
        if num < 0:
            print("Please enter a positive number!")
            return
            
        if is_strong_number(num):
            # Show calculation
            calculation = " + ".join(f"{digit}!" for digit in str(num))
            result = " + ".join(str(factorial(int(digit))) for digit in str(num))
            print(f"\n{num} is a strong number!")
            print(f"Calculation: {calculation} = {result} = {num}")
        else:
            print(f"\n{num} is not a strong number.")
            # Show calculation anyway
            calculation = " + ".join(f"{digit}!" for digit in str(num))
            result = " + ".join(str(factorial(int(digit))) for digit in str(num))
            total = sum(factorial(int(digit)) for digit in str(num))
            print(f"Calculation: {calculation} = {result} = {total} ≠ {num}")
            
    except ValueError:
        print("Please enter a valid integer!")

if __name__ == "__main__":
    check_strong_number()


## Naman Sethi 
