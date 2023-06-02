# Password Generator Project based on user defined amount of letters, 
# symbols and numbers to generate a random password.
import random
from characters import letters, symbols, numbers

# Welcome message and getting select number of letters, symbols and numbers
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = []
# password.extend(random.sample(letters, nr_letters))
# password.extend(random.sample(numbers, nr_numbers))
# password.extend(random.sample(symbols, nr_symbols))

password = [f"{l1}{l2}{l3}" for l1, l2, l3 in zip(random.sample(letters, nr_letters), random.sample(numbers, nr_numbers), random.sample(symbols, nr_symbols))]
print(f"Your password without any shuffling is: {''.join(password)}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(password)
print(f"Your password after shuffling is: {''.join(password)}")
