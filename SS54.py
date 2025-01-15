def are_anagrams():
    """Check if two strings are anagrams."""
    # Get input strings
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    
    # Remove spaces and convert to lowercase
    str1_cleaned = ''.join(str1.lower().split())
    str2_cleaned = ''.join(str2.lower().split())
    
    # Sort both strings and compare
    is_anagram = sorted(str1_cleaned) == sorted(str2_cleaned)
    
    # Display results
    print(f"\nString 1: {str1}")
    print(f"String 2: {str2}")
    
    if is_anagram:
        print("\nThese strings are anagrams!")
    else:
        print("\nThese strings are not anagrams.")
        
    # Show character frequency comparison
    if len(str1_cleaned) != len(str2_cleaned):
        print("(Different lengths after cleaning)")
    
    # Show sorted versions
    print(f"\nSorted characters:")
    print(f"String 1: {''.join(sorted(str1_cleaned))}")
    print(f"String 2: {''.join(sorted(str2_cleaned))}")

if __name__ == "__main__":
    are_anagrams()
