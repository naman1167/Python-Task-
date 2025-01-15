class Student:
    """A class to represent a student."""
    
    def __init__(self, name, student_id):
        """Initialize student with name and ID."""
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade):
        """Add a grade to student's record."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True
        print("Grade must be between 0 and 100!")
        return False
    
    def get_average(self):
        """Calculate average grade."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def get_letter_grade(self):
        """Convert numerical average to letter grade."""
        avg = self.get_average()
        if avg >= 90: return 'A'
        elif avg >= 80: return 'B'
        elif avg >= 70: return 'C'
        elif avg >= 60: return 'D'
        else: return 'F'
    
    def display_report(self):
        """Display student's grade report."""
        print("\nStudent Report Card")
        print("-" * 50)
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        
        if self.grades:
            print("\nGrades:")
            for i, grade in enumerate(self.grades, 1):
                print(f"Grade {i}: {grade}")
            
            print(f"\nNumber of grades: {len(self.grades)}")
            print(f"Average grade: {self.get_average():.2f}")
            print(f"Letter grade: {self.get_letter_grade()}")
            print(f"Highest grade: {max(self.grades)}")
            print(f"Lowest grade: {min(self.grades)}")
        else:
            print("\nNo grades recorded yet.")

def main():
    """Test the Student class."""
    try:
        # Create student
        name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        
        student = Student(name, student_id)
        
        while True:
            print("\n1. Add grade")
            print("2. View report card")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == '1':
                try:
                    grade = float(input("Enter grade (0-100): "))
                    student.add_grade(grade)
                except ValueError:
                    print("Please enter a valid number!")
            elif choice == '2':
                student.display_report()
            elif choice == '3':
                print("\nGoodbye!")
                break
            else:
                print("Invalid choice!")
                
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
