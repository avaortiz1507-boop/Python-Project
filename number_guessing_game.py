#1 ask user if they would like to play a guessing game
play_choice = input("Would you like to play a guessing game? (yes/no): ").strip().lower()
import random

def guess_number():
    secret_number: int = random.randint(1, 10)

    guess: int = 0

    while guess != secret_number:
        guess_input: str = input("Guess the number (between 1 and 10): ").strip()

        if not guess_input.isdigit():
            print("Invalid input. Please enter a number between 1 and 10.")
            continue

        guess: int = int(guess_input)

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number!")
            break


guess_number()

#2 python generates a random number between 1 and 10
#3 if yes, ask user to enter the number python is thinking
#4 if the user guesses the number correctly, print "Congratulations! You guessed the number!"
#5 if the user guesses the number incorrectly, print "Sorry, that's not the number. Try again!" and prompt the user to guess again
#6 continue the loop until the user guesses the number correctly or chooses to exit the game
