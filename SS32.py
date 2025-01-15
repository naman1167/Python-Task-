#Take a list of numbers from the user and find the maximum and minimum values.
lst = []
integers = input("Enter a list of numbers: ").split()
for i in integers:
    lst.append(int(i))
print("Maximum:", max(lst))
print("Minimum:", min(lst))
