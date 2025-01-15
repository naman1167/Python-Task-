import math

class Point:
    """A class to represent a point in 2D space."""
    
    def __init__(self, x=0, y=0):
        """Initialize point with x and y coordinates."""
        self.x = x
        self.y = y
    
    def set_coordinates(self, x, y):
        """Set new coordinates for the point."""
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        """Calculate distance from origin (0,0)."""
        return math.sqrt(self.x**2 + self.y**2)
    
    def distance_from_point(self, other):
        """Calculate distance from another point."""
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def quadrant(self):
        """Determine which quadrant the point is in."""
        if self.x > 0 and self.y > 0: return 1
        if self.x < 0 and self.y > 0: return 2
        if self.x < 0 and self.y < 0: return 3
        if self.x > 0 and self.y < 0: return 4
        if self.x == 0 and self.y == 0: return "Origin"
        if self.x == 0: return "Y-axis"
        if self.y == 0: return "X-axis"
    
    def __str__(self):
        """String representation of point."""
        return f"Point({self.x}, {self.y})"
    
    def display(self):
        """Display point details."""
        print(f"\nPoint Coordinates: ({self.x}, {self.y})")
        print(f"Distance from origin: {self.distance_from_origin():.2f}")
        print(f"Location: {self.quadrant()}")
        
        # Visual representation in ASCII
        self.plot()
    
    def plot(self, size=10):
        """Create a simple ASCII plot of the point."""
        print("\nVisual representation:")
        for y in range(size, -size-1, -1):
            for x in range(-size, size+1):
                if x == 0 and y == 0:
                    print("+", end="")
                elif x == 0:
                    print("|", end="")
                elif y == 0:
                    print("-", end="")
                elif round(x) == round(self.x) and round(y) == round(self.y):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

def main():
    """Test the Point class."""
    try:
        # Create first point
        print("First Point:")
        x1 = float(input("Enter x coordinate: "))
        y1 = float(input("Enter y coordinate: "))
        p1 = Point(x1, y1)
        
        # Create second point
        print("\nSecond Point:")
        x2 = float(input("Enter x coordinate: "))
        y2 = float(input("Enter y coordinate: "))
        p2 = Point(x2, y2)
        
        # Display information
        print("\nPoint 1:")
        p1.display()
        
        print("\nPoint 2:")
        p2.display()
        
        # Calculate distance between points
        distance = p1.distance_from_point(p2)
        print(f"\nDistance between points: {distance:.2f}")
        
    except ValueError:
        print("Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
