import os
from art import logo

def calculate_highest_bidder(all_bidders):
    highest_bid = 0
    highest_bidder = ""
    for bidder in all_bidders:
        bid = all_bidders[bidder]
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = bidder
    print(f"The winner is {highest_bidder.capitalize()} with a bid of R{highest_bid}")
            
continue_bidding = True
bidders = {}

while continue_bidding:
    os.system("cls||clear")
    print(f"Welcome to the secret auction!\n{logo}")
    
    name = input("Please enter your name: ").lower()
    bid = int(input("Please enter your bid: "))
    bidders[name] = bid
    
    if input("Are there any other bidders? Type 'yes' or 'no': ").lower() == "no":
        calculate_highest_bidder(bidders)
        continue_bidding = False