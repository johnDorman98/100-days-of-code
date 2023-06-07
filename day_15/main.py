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


# Set resouces and drinks from the data module.
resources = starting_resources
drinks = MENU
drink_options = get_drinks(drinks)

# Valid coins = penny: 0.01, nickel: 0.05, dime: 0.10, quarter: 0.25
coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25,
}

machine_on = True
enough_resources = True

# Coffee machine requirements.
while machine_on:
    # Start by getting input from the user with menu options based on the drinks from MENU.
    # Menu options will use the name of each drink within drinks, along with a secret report option and the option to exit.
    user_choice = input(
        f"What would you like to order: ({', '.join(drink_options)})"
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
        # If enough resources
        for resource in resources:
            if resources[resource] - selected_drink_resources[resource] < 0:
                enough_resources = False
                print(f"Sorry not enough {resource}.")
        
        if enough_resources:
            # Get coins from user
            total_coins = 0
            for coin in coins:
                insert_coin = int(input())
            # Compare total of inserted coins against the price of the selected drink
            # If enough coins
                # Take the required resouces away from the total resouces
                # Add the cost of the drink
                # Give change
                # Give x Drink
                # Return to menu
                
    # Else:
        # Show menu again with invalid message to user.