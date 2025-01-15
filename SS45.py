def manage_grades():
    """Manage student grades using a dictionary."""
    # Initialize student grades dictionary
    grades = {}
    
    while True:
        print("\n1. Add student grade")
        print("2. Look up student grade")
        print("3. Display all grades")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter student name: ")
            try:
                grade = float(input("Enter grade: "))
                grades[name] = grade
                print(f"Grade added for {name}")
            except ValueError:
                print("Please enter a valid numeric grade!")
                
        elif choice == '2':
            name = input("Enter student name to look up: ")
            if name in grades:
                print(f"{name}'s grade: {grades[name]}")
            else:
                print(f"No grade found for {name}")
                
        elif choice == '3':
            if grades:
                print("\nAll grades:")
                for name, grade in sorted(grades.items()):
                    print(f"{name}: {grade}")
            else:
                print("No grades recorded yet")
                
        elif choice == '4':
            break
            
        else:
            print("Invalid choice! Please enter 1-4")

if __name__ == "__main__":
    manage_grades()
