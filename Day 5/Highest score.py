# Day 5: Highest score in a list

# Input a list of student scores
student_scores = [145, 600, 700, 9000]

# Write your code below this row
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

# Print the highest score
print(f'The highest score is: {highest_score}')
