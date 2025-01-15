#Write a recursive function to compute the factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#Test the function with user input.
n = int(input("Enter a number: "))
print(factorial(n))
