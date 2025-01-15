#Input a positive integer n. Calculate the sum of the first n natural numbers.
num = int(input("Enter a positive integer: "))
sum = 0
for i in range(1, num + 1):
    sum += i
print("The sum of the first", num, "natural numbers is", sum)
