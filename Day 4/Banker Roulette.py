# Day 4: Banker Rouletter: Program that randomly selects someone to pay, can't use choice()

# import random module
import random

# Create a list of names
names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

# Get the length of names
names_len = len(names)

# Initiate a random selector
selector = random.randint(0, (names_len-1))

# Print the person to pay
print(f'{names[selector]} is going to buy the meal today!')