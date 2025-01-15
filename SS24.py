#Write a function is_prime(n) to check if a number n is prime. Test it with user input.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
