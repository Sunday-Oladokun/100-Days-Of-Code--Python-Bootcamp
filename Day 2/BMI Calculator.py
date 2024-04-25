# Day 2: Program that calculates Body Mass Index

# 1st input: enter height in meters
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