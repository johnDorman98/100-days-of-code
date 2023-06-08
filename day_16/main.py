# Importing classes from other modules for OOP.
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creating instances of each class.
menu_management = Menu()
money_management = MoneyMachine()
coffee_management = CoffeeMaker()
coffee_machine_on = True

while coffee_machine_on:

    # Stores a list of all the valid drink options.
    menu_options = menu_management.get_items()

    user_choice = input(f"What would you like: ({menu_options}): ").lower()
    
    # If the user_choice is a valid drink proceed.
    if user_choice in menu_options.split("/"):
        drink = menu_management.find_drink(user_choice)
        if coffee_management.is_resource_sufficient(drink):
            if money_management.make_payment(drink.cost):
                coffee_management.make_coffee(drink)
                
    elif user_choice == "report":
        coffee_management.report()
        money_management.report()
        
    elif user_choice == "off":
        print("Shutting down...")
        coffee_machine_on = False
        
    else:
        print("Sorry, invalid input detected.\n")