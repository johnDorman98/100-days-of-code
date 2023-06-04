############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Blackjack start
import random
import os
from art import logo


def deal_card():
    """Uses the random module to return a random card."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    random_card = random.choice(cards)
    return random_card


def calculate_score(hand):
    """Takes in a hand and returns the score."""

    return sum(hand)


def check_ace(hand):
    """Checks for an ace in the hand and if the score is greater than 21 turns it into a 1."""
    if 11 in hand and calculate_score(hand) > 21:
        hand[hand.index(11)] = 1

    return hand


def find_winner(user, computer):
    """Takes in ther user's and computer's hand to determine the winner of the game."""
    user_score = calculate_score(user)
    computer_score = calculate_score(computer)

    print(f"Your final hand {user} worth a total of {user_score}")
    print(f"Computer's final hand {computer} with a total of {computer_score}")

    if user_score == computer_score:
        print("Draw!")
    elif user_score > 21:
        print("Bust the computer wins.")
    elif computer_score > 21:
        print("You win the computer went bust.")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("You lose.")


def restart_blackjack():
    """Lets the user choose if they want to play another round."""
    if (
        input(
            "\nDo you want to play another round of Blackjack, type 'y' or 'n'"
        ).lower()
        == "y"
    ):
        # Using the os module to clear the terminal
        os.system("clear||cls")
        start_blackjack()
    else:
        print("Thank you for playing Blackjack.")
        return False


def check_for_blackjack(user, computer):
    """Takes in the user and computer hands to check for a Blackjack."""
    if (
        calculate_score(user) == calculate_score(computer)
        and 11 in user
        and 11 in computer
    ):
        print("Its a draw with Blackjack.")
        restart_blackjack()
    elif calculate_score(user) == 21 and 11 in user:
        print("You win with Blackjack!")
        restart_blackjack()
    else:
        print("Sorry, you lost the computer had Blackjack.")
        restart_blackjack()


# Welcome message.
def start_blackjack():
    """The main function which handles the games main logic and calls the other functions."""
    print(f"{logo}\nWelcome to my Blackjack game.")

    # Boolean to track the games loop.
    play_blackjack = True

    # Setting start hands for both the user and the computer.
    user_hand = []
    computer_hand = []

    # Deals two random cards for both user and computer.
    for i in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())

    while play_blackjack:
        # checks for an ace and calcualtes the users score. 
        # If an ace is found it can modify the hand if over 21.
        user_hand = check_ace(user_hand)
        computer_hand = check_ace(computer_hand)
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)

        print(f"Your hand {user_hand} worth a total of {calculate_score(user_hand)}")
        print(f"Computer's hand {computer_hand[0]}")

        # Depending on the users score the user is asked to either draw another card if they desire
        # if the went over 21 the winner is found and the game is reset.
        if user_score <= 21:
            next_card = input(
                "Do you want to draw another card, type 'y' or 'n': "
            ).lower()
        else:
            find_winner(user_hand, computer_hand)
            if restart_blackjack() == False:
                play_blackjack = False

        # If the user requests another card update their hand
        if next_card == "y":
            user_hand.append(deal_card())
        else:
            # The computers turn to draw while they have less then 17 as a score.
            while computer_score < 17:
                computer_hand.append(deal_card())
                computer_hand = check_ace(computer_hand)
                computer_score = calculate_score(computer_hand)

            # Find the winner through the function call.
            find_winner(user_hand, computer_hand)

            # Reset the game using user input.
            if restart_blackjack() == False:
                play_blackjack = False


start_blackjack()
