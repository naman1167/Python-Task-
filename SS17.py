#Input a positive integer and count how many digits it has
num = int(input("Enter a positive integer: "))
count = 0
while num != 0:
    count += 1
    num //= 10
    