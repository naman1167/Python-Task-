class ComplexNumber:
    """A class to represent complex numbers."""
    
    def __init__(self, real, imag):
        """Initialize complex number with real and imaginary parts."""
        self.real = real
        self.imag = imag
    
    def __str__(self):
        """String representation of complex number."""
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        return f"{self.real} - {abs(self.imag)}i"
    
    def __add__(self, other):
        """Add two complex numbers."""
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __sub__(self, other):
        """Subtract two complex numbers."""
        return ComplexNumber(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        """Multiply two complex numbers."""
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)
    
    def conjugate(self):
        """Return the complex conjugate."""
        return ComplexNumber(self.real, -self.imag)
    
    def magnitude(self):
        """Calculate the magnitude of the complex number."""
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    
    def display(self):
        """Display complex number details."""
        print(f"\nComplex Number: {self}")
        print(f"Real part: {self.real}")
        print(f"Imaginary part: {self.imag}")
        print(f"Magnitude: {self.magnitude():.2f}")
        print(f"Conjugate: {self.conjugate()}")

def main():
    """Test the ComplexNumber class."""
    try:
        print("First Complex Number:")
        real1 = float(input("Enter real part: "))
        imag1 = float(input("Enter imaginary part: "))
        c1 = ComplexNumber(real1, imag1)
        
        print("\nSecond Complex Number:")
        real2 = float(input("Enter real part: "))
        imag2 = float(input("Enter imaginary part: "))
        c2 = ComplexNumber(real2, imag2)
        
        # Display results
        print("\nOperations:")
        print(f"c1 = {c1}")
        print(f"c2 = {c2}")
        print(f"Addition: {c1 + c2}")
        print(f"Subtraction: {c1 - c2}")
        print(f"Multiplication: {c1 * c2}")
        
        # Display detailed information
        print("\nDetailed information for c1:")
        c1.display()
        print("\nDetailed information for c2:")
        c2.display()
        
    except ValueError:
        print("Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
