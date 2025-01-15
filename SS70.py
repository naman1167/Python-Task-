def sieve_of_eratosthenes():
    """Find prime numbers using Sieve of Eratosthenes algorithm."""
    try:
        n = int(input("Enter upper limit to find prime numbers: "))
        
        if n < 2:
            print("There are no prime numbers less than 2!")
            return
            
        # Initialize array of True values
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        # Apply Sieve of Eratosthenes
        steps = []
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Record numbers being marked as non-prime
                marked = []
                for j in range(i * i, n + 1, i):
                    if is_prime[j]:
                        marked.append(j)
                        is_prime[j] = False
                if marked:
                    steps.append((i, marked))
        
        # Collect prime numbers
        primes = [num for num, is_p in enumerate(is_prime) if is_p]
        
        # Display results
        print(f"\nPrime numbers up to {n}:")
        print(primes)
        print(f"\nTotal prime numbers found: {len(primes)}")
        
        # Show sieving steps
        if steps:
            print("\nSieving steps:")
            for prime, marked in steps:
                print(f"Marking multiples of {prime}: {marked}")
        
        # Additional statistics
        if primes:
            print(f"\nLargest prime found: {max(primes)}")
            print(f"Average gap between primes: {(primes[-1] - primes[0]) / (len(primes) - 1):.2f}")
            
    except ValueError:
        print("Please enter a valid integer!")

if __name__ == "__main__":
    sieve_of_eratosthenes()
