# Number guessing game.
import random

print("Welcome to the number guessing game.\nI'm thinking of a number between 1 and 100.")

EASY_GUESSES = 10
HARD_GUESSES = 5
play_guessing_game = True
random_number = random.randint(1, 100)

difficulty = input("Please choose a difficulty. Type '1' for easy, or '2' for hard: ")

guesses = EASY_GUESSES if difficulty == "1" else HARD_GUESSES

while play_guessing_game:
    if guesses > 0:
        print(f"You have {guesses} guesses left to guess the number")
        user_guess = int(input("Please make a guess: "))
        guesses -= 1
        
        if user_guess == random_number:
            print(f"You got it! The answer was {random_number}")
            play_guessing_game = False
        elif user_guess > random_number:
            print("Too high.")
        else:
            print("Too low.")
    else:
        print("Sorry, you ran out of guesses.")
        play_guessing_game = False
