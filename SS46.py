def display_dict_components():
    """Create a dictionary and display its keys and values separately."""
    # Create a sample dictionary
    sample_dict = {
        'name': 'John',
        'age': 25,
        'city': 'New York',
        'occupation': 'Engineer',
        'hobby': 'Reading'
    }
    
    print("Dictionary:", sample_dict)
    print("\nKeys:", list(sample_dict.keys()))
    print("Values:", list(sample_dict.values()))
    
    # Additional operations with keys and values
    print("\nKeys in alphabetical order:", sorted(sample_dict.keys()))
    print("Values in alphabetical order:", sorted(str(v) for v in sample_dict.values()))

if __name__ == "__main__":
    display_dict_components()
