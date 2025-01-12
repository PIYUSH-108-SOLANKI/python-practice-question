#Generate a random number. Prompt the user to guess until they get it right. Give hints (too high/too low).
import random
num = random.randint(1, 100)
attempts = 3
for i in range(attempts):
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == num:
        print("You got it!")
        break
    elif guess < num:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"Sorry, you've used all your attempts. The number was {num}.")
