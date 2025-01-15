#Input a positive integer and check if it’s a palindrome (same forwards and backwards).
num = int(input("Enter a positive integer: "))
temp = num
rev = 0
while num != 0:
    rev = rev * 10 + num % 10
    num //= 10
if temp == rev:
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
    