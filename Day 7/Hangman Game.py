# DAY 7: Hangman Game

# Import random for randomisation
import random

# Create a word list 
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)

# Print chosen word (debugging purpose only)
print(chosen_word)

# Create an empty List called display
display = []

# Fill the empty list with '-' for each letter in the random word
for letter in chosen_word:
    display.append('-')

# Print the blanks for the user to know how many guesses they have
print(display)

# Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user_guess = input('Guess a letter in the anonymous word\n').lower()
        
# Loop through each letter in the chosen word

while True:
    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    user_guess = input('Guess a letter in the anonymous word\n').lower()
   
    for letter in user_guess:
        if user_guess == letter:
            display.insert(chosen_word.index(letter), letter)
            print(display)
        else:
            display.insert(chosen_word.index(letter), letter)
            print(display)
            
        # Condition to break the loop when the word is fully guessed
        if '_' not in display:
        print("Congratulations! You've guessed the word:", ''.join(display))
        
        break