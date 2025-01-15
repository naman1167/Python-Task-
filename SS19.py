#Input a positive integer n. Sum up all even numbers and all odd numbers from 1 to n separately
num = int(input("Enter a positive integer: "))
sum_even = 0
sum_odd = 0
for i in range(1, num + 1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print("The sum of the first", num, "even numbers is", sum_even)
print("The sum of the first", num, "odd numbers is", sum_odd)
