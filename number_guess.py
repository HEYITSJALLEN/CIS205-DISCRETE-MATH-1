import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 1 and 100.")

while True:
    try:
        # Prompt the user for a guess
        guess = int(input("Enter your guess: "))
        
        # Check if the guess is correct, too low, or too high
        if guess == secret_number:
            print("Congratulations! You guessed the number!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
            
    except ValueError:
        # Handle the case where the input is not a valid integer
        print("Invalid input. Please enter a valid integer.")
