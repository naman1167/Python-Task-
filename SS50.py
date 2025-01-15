def check_name_in_set():
    """Check if a given name exists in a set of names."""
    # Create a sample set of names
    names_set = {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 
                 'Frank', 'Grace', 'Henry', 'Isabella', 'Jack'}
    
    print("Available names:", sorted(names_set))
    
    while True:
        # Get input from user
        name = input("\nEnter a name to check (or press Enter to exit): ").strip().capitalize()
        
        # Check if user wants to exit
        if not name:
            print("Goodbye!")
            break
            
        # Check membership
        if name in names_set:
            print(f"Yes, '{name}' is in the set!")
        else:
            print(f"No, '{name}' is not in the set.")
            # Suggest similar names (optional feature)
            similar_names = [n for n in names_set if n.startswith(name[0])]
            if similar_names:
                print(f"Similar names in the set: {', '.join(sorted(similar_names))}")

if __name__ == "__main__":
    check_name_in_set()
