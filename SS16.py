#Generate a random number. Prompt the user to guess until they get it right. Give hints (too high/too low).
import random
num = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
while guess != num:
    if guess < num:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess again: "))
print("You got it!")
