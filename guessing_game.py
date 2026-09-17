# Part 2: Number-Guessing Game, Extended
import random

# Generate a secret number between 1 and 100
secret_number = random.randint(1, 100)
max_guesses = 6
guesses_used = 0

print("Welcome to the Number-Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"You have {max_guesses} attempts to guess it!\n")

while guesses_used < max_guesses:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid whole number.")
        continue

    guesses_used += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed the secret number in {guesses_used} tries!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

    remaining = max_guesses - guesses_used
    if remaining > 0:
        print(f"Guesses remaining: {remaining}\n")

# If loop finishes without guessing the number
if guess != secret_number:
    print("\nOut of guesses!")
    print(f"The secret number was: {secret_number}")