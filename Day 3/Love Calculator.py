# Day 3: Love calculator

# Take input for both names
name1 = input('What is your name?\n')
name2 = input('What is their name?\n')

# Concatenate the two names
combined_name = name1 + name2

# Count occurence of each letter in true in the concatenated names
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

# Add the up the counts of each letter and string them
first_digit = str(t + r + u + e)

# Count occurence of each letter in love in the concatenated names
l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

# Add the up the counts of each letter and string them
second_digit = str(l + o + v + e)

# Compute love score as the concatenation of the counts above
love_score = first_digit + second_digit

# Convert the counts above to an integer
love_score_int = int(love_score) 

# Initiate a flow for checking the love score for compatibility
if (love_score_int < 10) or (love_score_int > 90):
    print("The love calculator is calculating your score")
    print(f"Your score is {love_score_int}, you go together like coke and mentos.")
elif (40 <= love_score_int <= 50):
    print("The love calculator is calculating your score")
    print(f"Your score is {love_score_int}, you are alright together.")
else:
    print(f"Your score is {love_score_int}")