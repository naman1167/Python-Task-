def count_vowels():
    """Count vowels in a string."""
    # Get input string
    text = input("Enter a string: ")
    
    # Define vowels
    vowels = 'aeiouAEIOU'
    
    # Count vowels
    vowel_count = {vowel: text.count(vowel) for vowel in vowels}
    
    # Calculate total
    total_vowels = sum(vowel_count.values())
    
    # Display results
    print(f"\nVowel count in '{text}':")
    for vowel in 'aeiou':
        lower_count = vowel_count[vowel]
        upper_count = vowel_count[vowel.upper()]
        if lower_count + upper_count > 0:
            print(f"'{vowel}' or '{vowel.upper()}': {lower_count + upper_count}")
    
    print(f"\nTotal vowels: {total_vowels}")

if __name__ == "__main__":
    count_vowels()
