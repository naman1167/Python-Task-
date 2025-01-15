def reverse_list(lst):
    """Reverse a list in place using two-pointer technique."""
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

def main():
    try:
        numbers = [int(x) for x in input("Enter integers separated by spaces: ").split()]
        print(f"Original list: {numbers}")
        reverse_list(numbers)
        print(f"Reversed list: {numbers}")
    except ValueError:
        print("Please enter valid integers!")

if __name__ == "__main__":
    main()
