def decimal_to_binary():
    """Convert decimal integer to binary."""
    try:
        decimal = int(input("Enter a decimal number: "))
        original = decimal
        
        if decimal < 0:
            print("Please enter a non-negative number!")
            return
            
        # Method 1: Using bin()
        binary1 = bin(decimal)[2:]  # Remove '0b' prefix
        
        # Method 2: Manual conversion
        if decimal == 0:
            binary2 = "0"
        else:
            binary2 = ""
            steps = []
            while decimal > 0:
                steps.append((decimal, decimal % 2))
                binary2 = str(decimal % 2) + binary2
                decimal //= 2
        
        # Display results
        print(f"\nDecimal number: {original}")
        print(f"Binary number: {binary1}")
        
        # Show conversion steps
        if original != 0:
            print("\nConversion steps:")
            for step in steps[::-1]:
                num, remainder = step
                print(f"{num} ÷ 2 = {num//2} remainder {remainder}")
        
        # Additional information
        print(f"\nBinary length: {len(binary1)} bits")
        print(f"Number of 1s: {binary1.count('1')}")
        print(f"Number of 0s: {binary1.count('0')}")
        
    except ValueError:
        print("Please enter a valid decimal number!")

if __name__ == "__main__":
    decimal_to_binary()



