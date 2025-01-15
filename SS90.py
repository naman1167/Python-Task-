class Employee:
    """Base class for all employees."""
    
    def __init__(self, name, emp_id, salary):
        """Initialize employee with basic attributes."""
        self.name = name
        self.emp_id = emp_id
        self._salary = salary  # Protected attribute
        self._attendance = []  # Track attendance
        self._performance = []  # Track performance ratings
    
    def get_salary(self):
        """Get employee's salary."""
        return self._salary
    
    def give_raise(self, amount):
        """Give employee a raise."""
        if amount > 0:
            self._salary += amount
            return True
        return False
    
    def add_attendance(self, date, status):
        """Add attendance record."""
        self._attendance.append({'date': date, 'status': status})
    
    def add_performance_rating(self, rating, comment):
        """Add performance rating."""
        if 1 <= rating <= 5:
            self._performance.append({'rating': rating, 'comment': comment})
            return True
        return False
    
    def get_average_performance(self):
        """Calculate average performance rating."""
        if not self._performance:
            return 0
        return sum(p['rating'] for p in self._performance) / len(self._performance)
    
    def display(self):
        """Display employee details."""
        print(f"\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"ID: {self.emp_id}")
        print(f"Salary: ${self._salary:,.2f}")
        print(f"Average Performance: {self.get_average_performance():.2f}/5.0")

class Manager(Employee):
    """Manager class, inheriting from Employee."""
    
    def __init__(self, name, emp_id, salary, department):
        """Initialize manager with additional attributes."""
        super().__init__(name, emp_id, salary)
        self.department = department
        self._team = []  # List of employees managed
        self._budget = 0  # Department budget
    
    def add_team_member(self, employee):
        """Add an employee to the team."""
        if employee not in self._team:
            self._team.append(employee)
            return True
        return False
    
    def remove_team_member(self, employee):
        """Remove an employee from the team."""
        if employee in self._team:
            self._team.remove(employee)
            return True
        return False
    
    def set_budget(self, amount):
        """Set department budget."""
        if amount >= 0:
            self._budget = amount
            return True
        return False
    
    def give_team_raise(self, percentage):
        """Give raise to all team members."""
        if percentage <= 0:
            return False
        
        total_raise = 0
        for employee in self._team:
            raise_amount = employee.get_salary() * (percentage / 100)
            if employee.give_raise(raise_amount):
                total_raise += raise_amount
        
        return total_raise
    
    def display(self):
        """Override display method to include manager-specific details."""
        super().display()
        print(f"Department: {self.department}")
        print(f"Team Size: {len(self._team)}")
        print(f"Department Budget: ${self._budget:,.2f}")
        
        if self._team:
            print("\nTeam Members:")
            for emp in self._team:
                print(f"- {emp.name} (ID: {emp.emp_id})")

def main():
    """Test the Employee and Manager classes."""
    try:
        # Create a manager
        print("Creating Manager:")
        name = input("Enter manager name: ")
        emp_id = input("Enter manager ID: ")
        salary = float(input("Enter manager salary: $"))
        department = input("Enter department: ")
        
        manager = Manager(name, emp_id, salary, department)
        manager.set_budget(1000000)  # Set $1M budget
        
        # Create some employees
        employees = []
        for i in range(2):
            print(f"\nCreating Employee {i+1}:")
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            salary = float(input("Enter employee salary: $"))
            
            emp = Employee(name, emp_id, salary)
            employees.append(emp)
            manager.add_team_member(emp)
        
        # Add some performance ratings
        manager.add_performance_rating(4, "Good leadership")
        manager.add_performance_rating(5, "Excellent project delivery")
        
        for emp in employees:
            emp.add_performance_rating(4, "Good work")
        
        # Give team raise
        raise_percentage = 5
        total_raise = manager.give_team_raise(raise_percentage)
        
        # Display information
        print("\nManager Information:")
        manager.display()
        
        print(f"\nTotal team raise given: ${total_raise:,.2f}")
        
    except ValueError:
        print("Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
