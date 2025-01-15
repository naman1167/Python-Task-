def concatenate_lists():
    """Concatenate two user input lists."""
    try:
        list1 = input("Enter first list elements separated by spaces: ").split()
        list2 = input("Enter second list elements separated by spaces: ").split()
        concatenated = list1 + list2
        print(f"First list: {list1}")
        print(f"Second list: {list2}")
        print(f"Concatenated list: {concatenated}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    concatenate_lists()
