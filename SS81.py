class Rectangle:
    """A class to represent a rectangle."""
    
    def __init__(self, length, width):
        """Initialize rectangle with length and width."""
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate area of rectangle."""
        return self.length * self.width
    
    def perimeter(self):
        """Calculate perimeter of rectangle."""
        return 2 * (self.length + self.width)
    
    def __str__(self):
        """String representation of rectangle."""
        return f"Rectangle(length={self.length}, width={self.width})"
    
    def display(self):
        """Display rectangle details."""
        print("\nRectangle Details:")
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")
        
        # Visual representation
        print("\nVisual representation:")
        for i in range(min(int(self.width), 10)):  # Limit to 10 rows for large rectangles
            print('*' * min(int(self.length), 20))  # Limit to 20 columns

def main():
    """Test the Rectangle class."""
    try:
        # Get input from user
        length = float(input("Enter length of rectangle: "))
        width = float(input("Enter width of rectangle: "))
        
        if length <= 0 or width <= 0:
            print("Length and width must be positive numbers!")
            return
            
        # Create rectangle object
        rect = Rectangle(length, width)
        rect.display()
        
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    main()
