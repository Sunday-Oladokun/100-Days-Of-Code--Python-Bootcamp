# Day 4: Heads or Tails Game

# Import random module
import random

# Set your coin tosser
coin = random.randint(0,1)

# Set control flow for result of the coin toss
if coin == 1:
  print("Heads")
else:
  print("Tails")