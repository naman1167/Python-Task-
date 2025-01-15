def get_prime_factors(n):
    """Find prime factors of a number."""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors

def prime_factorization():
    """Main function to find prime factors."""
    try:
        num = int(input("Enter a number to find its prime factors: "))
        original = num
        
        if num <= 0:
            print("Please enter a positive number!")
            return
            
        # Get prime factors
        factors = get_prime_factors(num)
        
        # Display results
        print(f"\nPrime factors of {original}: {factors}")
        
        # Show factorization steps
        if factors:
            print("\nFactorization steps:")
            current = original
            for factor in factors:
                print(f"{current} ÷ {factor} = {current//factor}")
                current //= factor
                
            # Show factorization in exponential form
            from collections import Counter
            factor_counts = Counter(factors)
            exponential_form = " × ".join(
                f"{factor}^{count}" if count > 1 else str(factor)
                for factor, count in sorted(factor_counts.items())
            )
            print(f"\nExponential form: {exponential_form}")
            
        else:
            print(f"{original} is 1 (no prime factors)")
            
    except ValueError:
        print("Please enter a valid integer!")

if __name__ == "__main__":
    prime_factorization()
