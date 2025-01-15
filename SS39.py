def find_common_elements():
    """Find common elements between two lists."""
    try:
        list1 = [int(x) for x in input("Enter first list integers separated by spaces: ").split()]
        list2 = [int(x) for x in input("Enter second list integers separated by spaces: ").split()]
        
        common = list(set(list1) & set(list2))
        print(f"First list: {list1}")
        print(f"Second list: {list2}")
        print(f"Common elements: {common}")
    except ValueError:
        print("Please enter valid integers!")

if __name__ == "__main__":
    find_common_elements()
