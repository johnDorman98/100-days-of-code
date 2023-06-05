# Imports needed for the program
import random
import os
from art import logo, vs
from game_data import data


def check_guess(a_followers, b_followers, guess):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def play_game():
    
    continue_guessing = True
    score = 0
    a_data = random.choice(data)
        
    while continue_guessing:

        # Display the logo
        print(logo)
        # Get two random items from data to start with
        b_data = random.choice(data)
        
        # Check if the two pieces of data is the same.
        while a_data == b_data:
            b_data = random.choice(data)
            
        a_followers_count = a_data["follower_count"]
        b_followers_count = b_data["follower_count"]
        
        # Display for the user to choose from.
        print(f'Compare A: {a_data["name"]}, a {a_data["description"]}, from {a_data["country"]}')
        print(vs)
        print(f'Compare B: {b_data["name"]}, a {b_data["description"]}, from {b_data["country"]}\n')
        
        # Ask user of for higher follower count
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        while user_guess not in ["a", "b"]:
                user_guess = input("Sorry, invalid input please type 'A' or 'B': ").lower()
                
        guessed_correctly = check_guess(a_followers_count, b_followers_count, user_guess)
        
        os.system("cls||clear")
        
        if guessed_correctly:
            score += 1
            print(f"You got it right! Score {score}\n")
        else:
            print(f"Sorry, you got it wrong. Score {score}")
            continue_guessing = False
            
play_game()