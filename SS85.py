class Car:
    """Base class for cars."""
    
    def __init__(self, make, model, year):
        """Initialize car with basic attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.fuel = 0
    
    def drive(self, distance):
        """Simulate driving the car."""
        if self.fuel > 0:
            self.odometer += distance
            self.fuel -= distance / 10  # Simple fuel consumption model
            return True
        return False
    
    def add_fuel(self, amount):
        """Add fuel to the car."""
        self.fuel += amount
    
    def get_info(self):
        """Get car information."""
        return {
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'odometer': self.odometer,
            'fuel': self.fuel
        }
    
    def display(self):
        """Display car details."""
        print(f"\n{self.year} {self.make} {self.model}")
        print(f"Odometer: {self.odometer} km")
        print(f"Fuel: {self.fuel:.1f} L")

class ElectricCar(Car):
    """Electric car class, inheriting from Car."""
    
    def __init__(self, make, model, year, battery_size):
        """Initialize electric car with battery size."""
        super().__init__(make, model, year)
        self.battery_size = battery_size
        self.charge_level = 0
    
    def charge(self, amount):
        """Charge the car's battery."""
        self.charge_level = min(100, self.charge_level + amount)
    
    def drive(self, distance):
        """Override drive method for electric car."""
        if self.charge_level > 0:
            self.odometer += distance
            self.charge_level -= distance / self.battery_size * 10
            return True
        return False
    
    def display(self):
        """Override display method for electric car."""
        super().display()
        print(f"Battery size: {self.battery_size} kWh")
        print(f"Charge level: {self.charge_level:.1f}%")

def main():
    """Test the Car and ElectricCar classes."""
    try:
        # Create regular car
        print("Regular Car Details:")
        make = input("Enter car make: ")
        model = input("Enter car model: ")
        year = int(input("Enter car year: "))
        
        car = Car(make, model, year)
        car.add_fuel(50)  # Add 50L of fuel
        car.drive(100)    # Drive 100km
        car.display()
        
        # Create electric car
        print("\nElectric Car Details:")
        make = input("Enter electric car make: ")
        model = input("Enter electric car model: ")
        year = int(input("Enter electric car year: "))
        battery = float(input("Enter battery size (kWh): "))
        
        ecar = ElectricCar(make, model, year, battery)
        ecar.charge(80)   # Charge to 80%
        ecar.drive(150)   # Drive 150km
        ecar.display()
        
    except ValueError:
        print("Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
