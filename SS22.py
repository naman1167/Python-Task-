#Write a function power(base, exponent) that returns base^exponent without using the built-in ** operator (use a loop)
def power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result