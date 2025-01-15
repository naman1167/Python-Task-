import math

class Circle:
    """A class to represent a circle."""
    
    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = radius
    
    def area(self):
        """Calculate area of circle."""
        return math.pi * self.radius ** 2
    
    def circumference(self):
        """Calculate circumference of circle."""
        return 2 * math.pi * self.radius
    
    def diameter(self):
        """Calculate diameter of circle."""
        return 2 * self.radius
    
    def __str__(self):
        """String representation of circle."""
        return f"Circle(radius={self.radius})"
    
    def display(self):
        """Display circle details."""
        print("\nCircle Details:")
        print(f"Radius: {self.radius}")
        print(f"Diameter: {self.diameter():.2f}")
        print(f"Area: {self.area():.2f}")
        print(f"Circumference: {self.circumference():.2f}")
        
        # Visual representation (ASCII art circle)
        self.draw_circle()
    
    def draw_circle(self):
        """Draw an ASCII art representation of the circle."""
        print("\nVisual representation:")
        size = min(int(self.radius * 2), 20)  # Limit size for large circles
        for i in range(size):
            for j in range(size):
                # Calculate if point is approximately on the circle
                x = i - size/2
                y = j - size/2
                if abs((x*x + y*y) - (size*size/4)) < size:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

def main():
    """Test the Circle class."""
    try:
        # Get input from user
        radius = float(input("Enter radius of circle: "))
        
        if radius <= 0:
            print("Radius must be a positive number!")
            return
            
        # Create circle object
        circle = Circle(radius)
        circle.display()
        
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()
