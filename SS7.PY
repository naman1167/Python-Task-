#Input a letter from the user and check if it’s a vowel or a consonant.
letter = input("Enter a letter: ")
if letter in "aeiouAEIOU":
    print(letter, "is a vowel.")
else:
    print(letter, "is a consonant.")
    