# Number Guessing Game - A beginner-friendly Python example
# Concepts: variables, input, loops, conditionals, random numbers

import random  # Import the random module to generate a secret number

# Computer picks a random number between 1 and 100 (inclusive)
secret_number = random.randint(1, 100)

# Greeting and instructions
print("Welcome to the Number Guessing Game!")
print("I've picked a number between 1 and 100.")
print("Try to guess it!")

attempts = 0  # Counter to track how many guesses the player makes

# Main game loop - keeps running until the player guesses correctly
while True:
    # Get input from the player
    guess_input = input("\nEnter your guess: ")
    
    # Safely convert input to an integer (handles non-number input)
    try:
        guess = int(guess_input)
    except ValueError:
        print("Oops! Please enter a valid whole number.")
        continue  # Go back to the start of the loop
    
    attempts += 1  # Increment the attempt counter (short for attempts = attempts + 1)
    
    # Check the guess and give feedback
    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        # Correct guess!
        print(f"Congratulations! 🎉 You got it in {attempts} attempts.")
        break  # Exit the loop and end the game

# End of game message
print("\nThanks for playing!")