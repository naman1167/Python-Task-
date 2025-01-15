def binary_to_decimal():
    """Convert binary string to decimal."""
    try:
        binary = input("Enter a binary number: ")
        
        # Validate binary input
        if not all(bit in '01' for bit in binary):
            print("Invalid binary number! Use only 0s and 1s.")
            return
            
        # Method 1: Using int() with base 2
        decimal1 = int(binary, 2)
        
        # Method 2: Manual conversion
        decimal2 = 0
        power = 0
        for bit in reversed(binary):
            decimal2 += int(bit) * (2 ** power)
            power += 1
            
        # Display results
        print(f"\nBinary number: {binary}")
        
        # Show calculation
        print("\nCalculation:")
        for i, bit in enumerate(reversed(binary)):
            if bit == '1':
                print(f"1 × 2^{i} = {2**i}")
        
        print(f"\nDecimal value: {decimal1}")
        
        # Additional information
        print(f"\nBinary length: {len(binary)} bits")
        print(f"Number of 1s: {binary.count('1')}")
        print(f"Number of 0s: {binary.count('0')}")
        
    except ValueError:
        print("Error converting to decimal!")

if __name__ == "__main__":
    binary_to_decimal()
