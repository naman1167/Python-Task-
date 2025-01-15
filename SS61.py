def is_armstrong(num):
    """Check if a number is an Armstrong number."""
    # Convert number to string to get digits
    num_str = str(num)
    power = len(num_str)
    
    # Calculate sum of digits raised to power
    digit_sum = sum(int(digit) ** power for digit in num_str)
    
    return digit_sum == num

def check_armstrong():
    """Main function to check Armstrong numbers."""
    try:
        num = int(input("Enter a number to check if it's an Armstrong number: "))
        if num < 0:
            print("Please enter a positive number!")
            return
            
        if is_armstrong(num):
            # Show calculation
            power = len(str(num))
            calculation = " + ".join(f"{digit}^{power}" for digit in str(num))
            result = " + ".join(str(int(digit) ** power) for digit in str(num))
            print(f"\n{num} is an Armstrong number!")
            print(f"Calculation: {calculation} = {result} = {num}")
        else:
            print(f"\n{num} is not an Armstrong number.")
            
    except ValueError:
        print("Please enter a valid integer!")

if __name__ == "__main__":
    check_armstrong()
