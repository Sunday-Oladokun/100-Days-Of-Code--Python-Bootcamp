# 100 DAYS OF PYTHON CODE WITH ANGELA YU
# DAY 03

# ODD OR EVEN NUMBER PROGRAM

# Prompt the user to enter a number and store their input in the variable user_input
user_input = input("Enter a number: ")

# Check if the user's input is a numeric value (i.e., an integer)
if user_input.isnumeric():
    # Convert the user's input to an integer and store it back in user_input
    user_input = int(user_input)

    # Check if the integer is even
    if user_input % 2 == 0:
        # If it's even, print a message indicating that it's an even number
        print(f"{user_input} is an even number.")
    else:
        # If it's not even (i.e., it's odd), print a message indicating that it's an odd number
        print(f"{user_input} is an odd number.")
else:
    # If the user's input is not a numeric value, print an error message
    print("Invalid input, please enter a valid numerical value.")

# PROGRAM THAT TESTS THE HEIGHT AND AGE OF PEOPLE BEFORE THEY CAN RIDE A ROLLERCOASTER    

print("Welcome to the rollercoaster!")

# Initialize an input that asks for height
height = int(input("What is your height in cm?\n"))

# Test the height against the threshold of 120cm 
if height >= 120:
  print("You can ride the rollercoaster")
  
  # Ask the user for their age
  age = int(input("What is your age?\n"))
  # Use the user's age to determine their bill
  if age < 12:
    print("Your bill is 5 dollars")
  elif age >= 12:
    print("Your bill is 7 dollars")
  else:
    print("Your bill is 12 dollars")
    
# User does not meet the primary requirement(120cm and above) to ride
else:
  print("Sorry, you are not old enough to ride the rollercoaster")
  
  
# PROGRAM THAT TAKE PIZZA ORDERS
#This program is optimized for adding pepperoni or extra cheese as well

print(("Welcome to Black Concept's Pizza Shop").upper())
print("Small pizza" " is" " S")
print("Medium pizza" " is" " M")
print("Large pizza" " is" " L")

bill = 0
s_pepperoni = 2
m_l_pepperoni = 3
extra_cheese = 1
order_size = input("What is the size of pizza that you want? S or M or L?\n").lower()

# Flow for Small Pizza Order
if order_size == "s":
  bill = 15

  wants_pepperoni = input("Do you want pepperoni? Y or N?\n").lower()
  wants_extra_cheese = input("Do you want extra cheese? Y or N?\n").lower()
  
  if wants_pepperoni == "y" and wants_extra_cheese == "y":
    bill += pepperoni + extra_cheese
    print(f"Thank you choosing Black Concept's Pizza Shop, Your total bill is {bill} dollars")

  if wants_pepperoni == "n" and wants_extra_cheese == "y":
    bill += extra_cheese
    print(f"Thank you choosing Black Concept's Pizza Shop, Your total bill is {bill} dollars")

  if wants_extra_cheese == "n" and wants_pepperoni == "y":
    bill += pepperoni
    print(f"Thank you choosing Black Concept's Pizza Shop, Your total bill is {bill} dollars")

  if wants_extra_cheese == "n" and wants_pepperoni == "n":
    print(f"Thank you choosing Black Concept's Pizza Shop, Your total bill is {bill} dollars")

  
elif order_size == "m":
  bill = 20

  wants_pepperoni = input("Do you want pepperoni? Y or N?\n").lower()
  wants_extra_cheese = input("Do you want extra cheese? Y or N?\n").lower()
  
  if wants_pepperoni == "y" and wants_extra_cheese == "y":
    bill += m_l_pepperoni + extra_cheese
    print(f"Thank you choosing Black Concept's Pizza Shop, Your total bill is {bill} dollars")

  if wants_pepperoni == "n" and wants_extra_cheese == "y":
    bill += extra_cheese
    print(f"Thank you choosing Black Concept's Pizza Shop, Your total bill is {bill} dollars")

  if wants_extra_cheese == "n" and wants_pepperoni == "y":
    bill += m_l_pepperoni
    print(f"Thank you choosing Black Concept's Pizza Shop, Your total bill is {bill} dollars")

  if wants_extra_cheese == "n" and wants_pepperoni == "n":
    print(f"Thank you choosing Black Concept's Pizza Shop, Your total bill is {bill} dollars")

else:
  bill = 25

  wants_pepperoni = input("Do you want pepperoni? Y or N?\n").lower()
  wants_extra_cheese = input("Do you want extra cheese? Y or N?\n").lower()
  
  if wants_pepperoni == "y" and wants_extra_cheese == "y":
    bill += m_l_pepperoni + extra_cheese
    print(f"Thank you choosing Black Concept's Pizza Shop, Your total bill is {bill} dollars")

  if wants_pepperoni == "n" and wants_extra_cheese == "y":
    bill += extra_cheese
    print(f"Thank you choosing Black Concept's Pizza Shop, Your total bill is {bill} dollars")

  if wants_extra_cheese == "n" and wants_pepperoni == "y":
    bill += m_l_pepperoni
    print(f"Thank you choosing Black Concept's Pizza Shop, Your total bill is {bill} dollars")

  if wants_extra_cheese == "n" and wants_pepperoni == "n":
    print(f"Thank you choosing Black Concept's Pizza Shop, Your total bill is {bill} dollars")
    
    
# PROGRAM THAT CALCULATES COMPATIBILITY (LOVE CALCULATOR)

# PROGRAM THAT CALCULATES COMPATIBILITY (LOVE CALCULATOR)
name1 = input("Enter your name\n").lower()
name2 = input("Enter your name\n").lower()

combined_name = name1 + name2

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

first_digit = str(t + r + u + e)

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

second_digit = str(l + o + v + e)
love_score = first_digit + second_digit
love_score_int = int(love_score) 


if (love_score_int < 10) or (love_score_int > 90):
    print("The love calculator is calculating your score")
    print(f"Your score is {love_score_int}, you go together like coke and mentos.")
elif (40 <= love_score_int <= 50):
    print("The love calculator is calculating your score")
    print(f"Your score is {love_score_int}, you are alright together.")
else:
    print(f"Your score is {love_score_int}")


# TREASURE ISLAND GAME

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")

start = input("Do you want to go left or right? ").lower()

if start == "left":
  stage2 = input("Would you like to swim or wait? ").lower()

  if stage2 == "wait":
    stage3 = input("Which do you want to open: red or blue or yellow? ").lower()

    if stage3 == "yellow":
      print("You Win!!!")
    
    elif stage3 == "blue":
      print("You got eaten by beasts, Game over!!!")

    elif stage3 == "red":
      print("You got burned by fire, Game over!!!")

    else:
      print("Game over!!!")

  else:
    print("You got attacked by a trout, Game over!!!")

else:
  print("You have fallen into a hole, Game over!!!")