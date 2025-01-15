#Write a function count_occurrences(lst, x) that returns how many times x appears in the list lst.
def count_occurrences(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count
#Test the function with user input.
lst = [int(x) for x in input("Enter a list of numbers: ").split()]
x = int(input("Enter a number: "))
print(count_occurrences(lst, x))
