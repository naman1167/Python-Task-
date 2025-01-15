#Write a function lcm(a, b) that finds the least common multiple of a and b. Hint: lcm(a, b) = abs(a*b)/gcd(a,b)
import SS26
def lcm(a, b):
    return abs(a*b)/gcd(a,b)
#Test the function with user input.
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(lcm(a, b))