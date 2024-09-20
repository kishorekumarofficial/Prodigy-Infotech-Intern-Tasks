import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    # Loop until the user guesses the correct number
    while not guessed:
        try:
            # Ask the user for their guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1  # Increment the attempt counter

            # Check if the guess is too high, too low, or correct
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly.")
                print(f"It took you {attempts} attempts.")
        except ValueError:
            print("Please enter a valid number!")

# Run the game
guess_the_number()
