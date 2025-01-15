def gcd(a, b):
    """Calculate GCD using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate LCM using GCD."""
    return abs(a * b) // gcd(a, b)

def lcm_range():
    """Calculate LCM of numbers in a range."""
    try:
        n = int(input("Enter the upper limit of range [1..n]: "))
        
        if n <= 0:
            print("Please enter a positive number!")
            return
            
        # Calculate LCM progressively
        result = 1
        steps = []
        
        for i in range(1, n + 1):
            old_result = result
            result = lcm(result, i)
            steps.append((i, old_result, result))
        
        # Display results
        print(f"\nLCM of numbers from 1 to {n}: {result}")
        
        # Show calculation steps
        print("\nStep by step calculation:")
        for i, old, new in steps:
            if i == 1:
                print(f"LCM(1) = 1")
            else:
                print(f"LCM({old}, {i}) = {new}")
        
        # Additional information
        print(f"\nFactors of final LCM:")
        factors = []
        temp = result
        d = 2
        while temp > 1:
            while temp % d == 0:
                factors.append(d)
                temp //= d
            d += 1
            if d * d > temp:
                if temp > 1:
                    factors.append(temp)
                break
        
        from collections import Counter
        factor_counts = Counter(factors)
        for factor, count in sorted(factor_counts.items()):
            print(f"{factor}: {count} time(s)")
            
    except ValueError:
        print("Please enter a valid integer!")

if __name__ == "__main__":
    lcm_range()








