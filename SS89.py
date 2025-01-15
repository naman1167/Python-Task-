class Temperature:
    """A class to demonstrate property decorators."""
    
    def __init__(self, celsius=0):
        """Initialize temperature in Celsius."""
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Get temperature in Celsius."""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Set temperature in Celsius."""
        if value < -273.15:  # Absolute zero
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Get temperature in Fahrenheit."""
        return (self.celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Set temperature in Fahrenheit."""
        self.celsius = (value - 32) * 5/9
    
    @property
    def kelvin(self):
        """Get temperature in Kelvin."""
        return self.celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        """Set temperature in Kelvin."""
        self.celsius = value - 273.15
    
    def display(self):
        """Display temperature in all units."""
        print("\nTemperature Readings:")
        print(f"Celsius: {self.celsius:.2f}°C")
        print(f"Fahrenheit: {self.fahrenheit:.2f}°F")
        print(f"Kelvin: {self.kelvin:.2f}K")

def main():
    """Test the Temperature class."""
    try:
        temp = Temperature()
        
        while True:
            print("\n1. Set Celsius")
            print("2. Set Fahrenheit")
            print("3. Set Kelvin")
            print("4. Display Temperature")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == '1':
                celsius = float(input("Enter temperature in Celsius: "))
                temp.celsius = celsius
            elif choice == '2':
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                temp.fahrenheit = fahrenheit
            elif choice == '3':
                kelvin = float(input("Enter temperature in Kelvin: "))
                temp.kelvin = kelvin
            elif choice == '4':
                temp.display()
            elif choice == '5':
                print("\nGoodbye!")
                break
            else:
                print("Invalid choice!")
                
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
