from art import logo


def add(n1, n2):
    """Takes two numbers and returns the total after adding the numbers."""
    return n1 + n2


def subtract(n1, n2):
    """Takes two numbers and returns the total after subtracting the numbers."""
    return n1 - n2


def multiply(n1, n2):
    """Takes two numbers and returns the total after multiply the numbers."""
    return n1 * n2


def divide(n1, n2):
    """Takes two numbers and returns the total after divide the numbers."""
    return n1 / n2


operators = {"+": add, "-": subtract, "*": multiply, "/": divide}
continue_calculating = True


def calculator():
    print(logo)
    num1 = float(input("What is the first number: "))

    while continue_calculating:

        for symbol in operators:
            print(symbol)

        selected_operator = input("Please select an operator from the above menu: ")

        num2 = float(input("What is the next number: "))

        answer = operators[selected_operator](num1, num2)

        print(f"{num1} {selected_operator} {num2} = {answer}")
        
        new_status = input(f"Type 'y' to contiue calculating with {answer}, type 's' to start a new calculation or type 'n' to exit: ").lower()
        
        if new_status == "y":
            num1 = answer
        elif new_status == "s":
            calculator()
        else:
            continue_calculating = False
            return
    

calculator()
