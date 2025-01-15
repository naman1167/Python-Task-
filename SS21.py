#Write four functions: add(a, b), subtract(a, b), multiply(a, b), and divide(a, b). Then prompt the user for two numbers and the operation. Use the corresponding function to output the result.
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ")
if operation == "add":
    print("The sum of", num1, "and", num2, "is", add(num1, num2))
elif operation == "subtract":
    print("The difference of", num1, "and", num2, "is", subtract(num1, num2))
elif operation == "multiply":
    print("The product of", num1, "and", num2, "is", multiply(num1, num2))
elif operation == "divide":
    print ("The division of", num1, "and", num2, "is", divide(num1, num2))
else:
    print("Invalid operation.")
    