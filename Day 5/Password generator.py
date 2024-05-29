# Day 5: Password Generator

# Import random module
import random

# Create letters of the alphabet, capitalised and non-capitalised as a list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Create the numbers as a list
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Create symbols as a list
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get the length of each lists
len_letters = len(letters)
len_numbers = len(numbers)
len_symbols = len(symbols)

# Welcome the user
print("Welcome to the PyPassword Generator!")

# Request for how many letters for password
nr_letters= int(input("How many letters would you like in your password?\n"))

# Request for how many numbers for password
nr_symbols = int(input(f"How many numbers would you like?\n"))

# Request for how many symbols for password
nr_numbers = int(input(f"How many symbols would you like?\n"))

#PASSWORD FLOW2

# Create a password container
easy_password = []

for entry in range(0, (nr_letters)):
    letters_p = random.choice(letters)
    easy_password.append(letters_p)
    
for entry in range(0, (nr_numbers)):
    numbers_p = random.choice(numbers)
    easy_password.append(numbers_p)

for entry in range(0, (nr_symbols)):
    symbols_p = random.choice(numbers)
    easy_password.append(symbols_p)

# Randomise password or not
randomise = input('Do you want the password to be randomised? (Y or N)\n').lower()

if randomise == 'y':
    random.shuffle(easy_password)
    password = ""
    
    for entry in easy_password:
        password += entry
    
    print(f'Your password is: {password}')

else:
    password = ""
    
    for entry in easy_password:
        password += entry
    print(f'Your password is: {password}')