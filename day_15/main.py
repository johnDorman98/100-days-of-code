# Imports
from coffe_data import MENU, starting_resources


def get_drinks(drinks):
    """Takes in the drinks dictionary and returns the drink options."""
    all_drinks = []
    for drink in drinks:
        all_drinks.append(drink)
        
    return all_drinks


def generate_report(resources):
    """Takes in all the current resouces and is used to display the
    resouces available"""
    for recource in resources:
        print(f"{recource.capitalize()}: {resources[recource]}")


def check_resources(resources, selected_drink_resources):
    """Takes in the dictionary of resources and the required resources 
    for the selected drink and returns True if there are enough resources."""
    enough_recources = True
    
    for resource in resources:
        if resource != "money":
            if resources[resource] - selected_drink_resources[resource] < 0:
                print(f"Sorry not enough {resource}.")
                enough_recources = False
        
    return enough_recources


def get_coins_inserted(coins):
    """Takes in the dictionary of accepted coins and asks the user how many 
    of each coin they wish to insert along with validation to ensure 
    correct coins and inputs are being entered."""
    total_inserted_coins = 0
    
    print(
        "Please enter the amount of each of the below coins"
        " you are inserting.\n"
    )
    
    for coin in coins:
        while True:
            try:
                insert_coin_amount = int(input(f"How many {coin}({coins[coin]:.2f}c): "))
                            
                if insert_coin_amount < 0:
                    print(
                        "Please enter 0 for no coins or amounts"
                        f" greater than 0 if you are adding any {coin}"
                    )
                    continue
                            
                total_inserted_coins += coins[coin] * insert_coin_amount
                print(total_inserted_coins)
                break
            except TypeError:
                print(
                    "Please enter the number of coins you inserted in a" 
                    f" number format, e.g '3' if three {coin:.2f} are"
                    " being inserted."                            
                )
                continue
    return total_inserted_coins


def coffee_machine(resources, drinks, drink_options, coins):
    """This is the main application that houses all the logic 
    for the coffee machine and is responsible for calling the other functions."""
    machine_on = True

    # Coffee machine requirements.
    while machine_on:
        # Start by getting input from the user with menu options based on the drinks from MENU.
        # Menu options will use the name of each drink within drinks, along with a secret report option and the option to exit.
        user_choice = input(
            f"What would you like to order: ({', '.join(drink_options)}): "
        ).lower()
        
        # If user selects report
        if user_choice == "report":
            # Display a report of the current resouces
            generate_report(resources)
        # If exit
        elif user_choice == "exit":
            # Exit the program turning off the machine
            print("Shutting down...")
            break
            
        # If drink is valid
        elif user_choice in drink_options:
            selected_drink_resources = drinks[user_choice]["ingredients"]
            selected_drink_cost = drinks[user_choice]["cost"]
            # If enough resources
            
            
            if check_resources(resources, selected_drink_resources):
                # Get coins from user
                total_inserted_coins = get_coins_inserted(coins)
                        
                # Compare total of inserted coins against the price of the selected drink
                # If enough coins
                if total_inserted_coins >= selected_drink_cost:
                    change = total_inserted_coins - selected_drink_cost
                    # Take the required resouces away from the total resouces
                    for resource in resources:
                        if resource != "money":
                            resources[resource] -= selected_drink_resources[resource]
                    # Add the cost of the drink
                    resources["money"] += selected_drink_cost
                    # Give change
                    if change > 0:
                        print(f"Here is your change: {change}")
                    # Give x Drink
                    print(f"Here is your {user_choice}. Enjoy!")
                    # Return to menu
                else:
                    print("Sorry, not enough money was added the"
                        f" drink costs {selected_drink_cost:.2f}."
                        f" Here is your refunded money {total_inserted_coins:.2f}"
                    )
        else:
            # Show menu again with invalid message to user.
            print("Invalid menu option please try again.")


# Set resouces and drinks from the data module.
resources = starting_resources
resources["money"] = 0

drinks = MENU
drink_options = get_drinks(drinks)

# Valid coins = penny: 0.01, nickel: 0.05, dime: 0.10, quarter: 0.25
coins = {
    "pennies": 0.01,
    "nickels": 0.05,
    "dimes": 0.10,
    "quarters": 0.25,
}

coffee_machine(resources, drinks, drink_options, coins)