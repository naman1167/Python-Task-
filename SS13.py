#input a positive integer and print its multiplication table (e.g., 1 to 10).
num = int(input("Enter a positive integer: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
    
