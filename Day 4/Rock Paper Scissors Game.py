# Day 4: Rock, Paper, Scissors Game

# Import random module
import random

# Initialize rock, paper, scissors symbols
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Initialize a list of choices for computer
computer_list = ['r', 'p', 's']

# Get player name
player_name = input('What is your name?')
print(f'Welcome to the rock, paper, scissors game {player_name}!')

# Start program flow
while True: # The program keeps playing until stopped
    print("You can make a choice by entering 'R', 'P', or 'S' or enter 'STOP' to stop the game")
    
    player_choice = input('Rock(R), Paper(P), or Scissors(S) OR STOP?').lower()
    
    if player_choice not in ['r', 'p', 's', 'stop']:
        print('You have made an invalid entry')
        break

    computer_choice = random.choice(computer_list)
    
    if player_choice == 'stop':
        print('Game Over')
        break
    
    else:  
        # Player wins scenarios
        if player_choice == 'r' and computer_choice == 's':
            print(rock)
            print('---------------------------------------------------------------------------')
            print(scissors)
            print(f'{player_name} wins')
        elif player_choice == 'p' and computer_choice == 'r':
            print(paper)
            print('---------------------------------------------------------------------------')
            print(rock)
            print(f'{player_name} wins')
        elif player_choice == 's' and computer_choice == 'p':
            print(scissors)
            print('---------------------------------------------------------------------------')
            print(paper)
            print(f'{player_name} wins')
            
        # Computer wins scenarios
        elif player_choice == 's' and computer_choice == 'r':
            print(scissors)
            print('---------------------------------------------------------------------------')
            print(rock)
            print('Computer wins')
        elif player_choice == 'r' and computer_choice == 'p':
            print(rock)
            print('---------------------------------------------------------------------------')
            print(paper)
            print('Computer wins')
        elif player_choice == 'p' and computer_choice == 's':
            print(paper)
            print('---------------------------------------------------------------------------')
            print(scissors)
            print('Computer wins')
            
        else:
            print('Its a draw')