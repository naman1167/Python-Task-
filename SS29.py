#Write a recursive function to solve the Tower of Hanoi puzzle for n disks.
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print("Move disk", n, "from", source, "to", target)
    tower_of_hanoi(n-1, auxiliary, target, source)
#Test the function with user input.
n = int(input("Enter the number of disks: "))
tower_of_hanoi(n, 'A', 'C', 'B')
#Output:
#Enter the number of disks: 3
#Move disk 1 from A to C
#Move disk 2 from A to B
#Move disk 1 from C to B
#Move disk 3 from A to C
#Move disk 1 from B to A
#Move disk 2 from B to C
#Move disk 1 from A to C
