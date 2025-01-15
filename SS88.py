class DateUtil:
    """A class to demonstrate different method types."""
    
    def __init__(self, year, month, day):
        """Initialize date with year, month, and day."""
        self.year = year
        self.month = month
        self.day = day
    
    def display_date(self):
        """Instance method: Display the date."""
        return f"{self.year}-{self.month:02d}-{self.day:02d}"
    
    @classmethod
    def from_string(cls, date_string):
        """Class method: Create DateUtil object from string."""
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @staticmethod
    def is_leap_year(year):
        """Static method: Check if a year is leap year."""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    @classmethod
    def get_month_days(cls, year, month):
        """Class method: Get number of days in a month."""
        days_in_month = {
            1: 31, 2: 29 if cls.is_leap_year(year) else 28,
            3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31,
            11: 30, 12: 31
        }
        return days_in_month.get(month)
    
    def is_valid_date(self):
        """Instance method: Check if the date is valid."""
        if not (1 <= self.month <= 12):
            return False
        
        max_days = self.get_month_days(self.year, self.month)
        return 1 <= self.day <= max_days

def main():
    """Demonstrate different method types."""
    try:
        # Using instance method
        print("Creating a date object...")
        date = DateUtil(2024, 2, 29)
        print(f"Instance method - display_date(): {date.display_date()}")
        print(f"Is valid date?: {date.is_valid_date()}")
        
        # Using class method
        print("\nCreating date from string...")
        date_string = "2024-12-25"
        date2 = DateUtil.from_string(date_string)
        print(f"Class method - from_string(): {date2.display_date()}")
        
        # Using static method
        year = 2024
        print(f"\nChecking if {year} is leap year...")
        print(f"Static method - is_leap_year(): {DateUtil.is_leap_year(year)}")
        
        # Using class method with static method
        year = 2024
        month = 2
        print(f"\nChecking days in month {month} of {year}...")
        days = DateUtil.get_month_days(year, month)
        print(f"Class method - get_month_days(): {days}")
        
        # Interactive testing
        print("\nTest your own date:")
        year = int(input("Enter year: "))
        month = int(input("Enter month (1-12): "))
        day = int(input("Enter day: "))
        
        test_date = DateUtil(year, month, day)
        print(f"\nDate: {test_date.display_date()}")
        print(f"Is valid?: {test_date.is_valid_date()}")
        print(f"Is leap year?: {DateUtil.is_leap_year(year)}")
        print(f"Days in month: {DateUtil.get_month_days(year, month)}")
        
    except ValueError:
        print("Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
