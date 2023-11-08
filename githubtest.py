# githubtest
import random

# Generate a random number between 1 and 20
secret_number = random.randint(1, 20)

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 20.")

# Initialize the number of attempts
attempts = 0

# Main game loop
for attempts in range(1, 6):
    # Ask the player for their guess
    guess = int(input("Take a guess: "))

    # Check if the guess is correct
    if guess == secret_number:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# If the player runs out of attempts, reveal the secret number
if attempts == 5:
    print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
