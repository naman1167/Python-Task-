#Write a function gcd(a, b) that computes the greatest common divisor of a and b.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#Test the function with user input.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(gcd(a, b))



