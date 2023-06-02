import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_choice = random.randint(0,2)

game_outcome = [user_choice, computer_choice]

if user_choice == computer_choice:
    print("It's a draw!")
elif game_outcome == [0,2] or game_outcome == [1,0] or game_outcome == [2,1]:
    print("You win!")
else:
    print("You lose!")