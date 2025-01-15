#Input a positive integer and reverse its digits (e.g., 123 -> 321)
num = int(input("Enter a positive integer: "))
rev = 0
while num != 0:
    rev = rev * 10 + num % 10
    num //= 10
    