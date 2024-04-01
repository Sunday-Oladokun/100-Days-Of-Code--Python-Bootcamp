# 100 DAYS OF CODE WITH ANGELA YU
# DAY 02 

# Program that takes two integer inputs and returns their sum

# Initialize an input function requesting for a 2 digit number
two_digit_number = input("Enter a two digit number\n")
# Cast the input as a string so you can index it
str_two_digit_number = str(two_digit_number)
# Sum the indexed values by casting them in an integer for summation to work... If you don't do this, the two digits will be concatenated
summation = (int(str_two_digit_number[0]) + int(str_two_digit_number[1]))
# Print final result
print(summation)

# Program that calculates Body Mass Index

height = float(input('What is your height?\n'))
# 2nd input: enter weight in kilograms e.g: 72
weight = float(input('What is your weight?\n'))
# Body Mass Index = weight/height**2
BMI = round(weight / (height ** 2), 2)
if BMI < 18.5:
  print(f"Your Body Mass Index is {BMI}, you are underweight")
elif BMI >= 18.5 and BMI < 25:
  print(f"Your Body Mass Index is {BMI}, you are normal weight")
elif BMI >= 25 and BMI < 30:
  print(f"Your Body Mass Index is {BMI}, you are overweight")
else:
  print(f"Your Body Mass Index is {BMI}, you are obese")

# Program that calculates Body Mass Index... As a function

# The function calculates the BMI to 2 decimal places
def Body_Mass_Index(height, weight):
  BMI = round(weight / (height ** 2), 2)
  if BMI < 18.5:
    print(f"Your Body Mass Index is {BMI}, you are underweight")
  elif BMI >= 18.5 and BMI < 25:
    print(f"Your Body Mass Index is {BMI}, you are normal weight")
  elif BMI >= 25 and BMI < 30:
    print(f"Your Body Mass Index is {BMI}, you are overweight")
  else:
    print(f"Your Body Mass Index is {BMI}, you are obese")

# Program that calculates how many weeks left to live with reference to 90 years lifespan
age = input("What is your age?\n")
weeks_left = (90 - int(age)) * 52
print(f"You have {weeks_left} weeks left.")

