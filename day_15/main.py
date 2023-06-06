# Imports
from coffe_data import MENU, starting_resources

# Set resouces and drinks from the data module.
resources = starting_resources
drinks = MENU

# Valid coins = penny: 0.01, nickel: 0.05, dime: 0.10, quartar: 0.25

# Coffee machine requirements.
# Start by getting input from the user with menu options based on the drinks from MENU.
# Menu options will use the name of each drink within drinks, along with a secret report option and the option to exit.
# If user selects report
    # Display a report of the current resouces
# If exit
    # Exit the program turning off the machine
# If drink is valid
    # If enough resources
        # Get coins from user
        # Compare total of inserted coins against the price of the selected drink
        # If enough coins
            # Take the required resouces away from the total resouces
            # Add the cost of the drink
            # Give change
            # Give x Drink
            # Return to menu
    # ELse
        # Sorry not enough of x resource
        # Return to menu
# Else:
    # Show menu again with invalid message to user.