def get_proper_divisors(num):
    """Get all proper divisors of a number."""
    divisors = [1]  # 1 is always a proper divisor
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:  # Avoid adding the same divisor twice for perfect squares
                divisors.append(num // i)
    return sorted(divisors)

def is_perfect_number(num):
    """Check if a number is perfect."""
    if num <= 1:
        return False
    return sum(get_proper_divisors(num)) == num

def check_perfect_number():
    """Main function to check perfect numbers."""
    try:
        num = int(input("Enter a number to check if it's perfect: "))
        if num <= 0:
            print("Please enter a positive number!")
            return
            
        divisors = get_proper_divisors(num)
        divisor_sum = sum(divisors)
        
        print(f"\nProper divisors of {num}: {divisors}")
        print(f"Sum of proper divisors: {' + '.join(map(str, divisors))} = {divisor_sum}")
        
        if is_perfect_number(num):
            print(f"\n{num} is a perfect number!")
        else:
            print(f"\n{num} is not a perfect number.")
            
        # Additional info
        if divisor_sum < num:
            print(f"{num} is deficient by {num - divisor_sum}")
        elif divisor_sum > num:
            print(f"{num} is abundant by {divisor_sum - num}")
            
    except ValueError:
        print("Please enter a valid integer!")

if __name__ == "__main__":
    check_perfect_number()
