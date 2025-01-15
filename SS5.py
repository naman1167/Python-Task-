#Prompt for two variables and swap their values. Show the results before and after swapping.
var1 = input("Enter a variable: ")
var2 = input("Enter another variable: ")
print("Before swapping:")
print("var1 =", var1)
print("var2 =", var2)
temp = var1
var1 = var2
var2 = temp
print("After swapping:")
print("var1 =", var1)
print("var2 =", var2)
