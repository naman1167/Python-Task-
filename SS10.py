#Input principal, rate, and time. Compute the simple interest as SI = (principal * rate * time) /  100. Display the result.
principal = float(input("Enter the principal: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the time: "))
simple_interest = (principal * rate * time) / 100
print("The simple interest is", simple_interest)
print("The amount is", principal + simple_interest)
