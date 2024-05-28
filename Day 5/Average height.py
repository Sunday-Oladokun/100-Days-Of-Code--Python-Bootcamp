# Day 5: Average Height Program

# Create a list of heights
heights = [151, 145, 179]
summation = 0

# Create a loop that sums the heights
for height in heights:
    summation = summation + height

# Get the length of the list
list_length = len(heights)

# Calculate the average height
average_height = summation / list_length

# Print the average height    
print(average_height)


# ALTERNATIVELY
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Height sum variable
height_sum = 0

# Loop for summing all heights
for height in student_heights:
  height_sum += height

# print total height summed
print(f'total height = {height_sum}')

# Student sum variable
students_num = 0

# Loop for counting number of students
for student in student_heights:
  students_num += 1

# Print number of students
print(f'number of students = {students_num}')

# Average height of students
average_height = round(height_sum / students_num)
print(f'average height = {average_height}')