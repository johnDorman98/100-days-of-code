#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Getting the necessary inputs to calcualte the total bill for each person.
total_without_tip = float(input("Please enter the total of the bill: R"))
amount_of_people = int(input("Please enter the number of people that is splitting the bill: "))
tip = float(input("Please enter the tip percentage without the % sign: "))

# Calculating the total for each person and displaying it.
total_per_person = (total_without_tip / amount_of_people) * (1 + (tip / 100))
print(f"The total amount that each person should pay is: R{total_per_person:.2f}")