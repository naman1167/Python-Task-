def element_wise_sum():
    """Calculate element-wise sum of two lists of equal length."""
    try:
        list1 = [float(x) for x in input("Enter first list numbers separated by spaces: ").split()]
        list2 = [float(x) for x in input("Enter second list numbers separated by spaces: ").split()]
        
        if len(list1) != len(list2):
            print("Lists must be of equal length!")
            return
            
        result = [x + y for x, y in zip(list1, list2)]
        print(f"First list: {list1}")
        print(f"Second list: {list2}")
        print(f"Element-wise sum: {result}")
        
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    element_wise_sum()
