# DAY 2: Tip Calculator

# Opening message
print('Hello, welcome to the tip calculator')

# Enter the total bill
total_bill = float(input('What is the total bill($)?\n'))

# Enter number of people
num_people = int(input('How many people are splitting the bill?\n'))

# Enter the tip percentage
tip_percentage = int(input('What percentage tip would you like to give?\n'))

# Calculate the total tip amount ($)
total_tip = total_bill * (tip_percentage / 100)

# Each person is to pay
each_person_pay = (total_bill + total_tip) / total_tip

print('------------------------------------------------------------------')

# Print the total bill, tip amount, and each person's pay
print(f'The total bill is ${total_bill:.2f}')
print(f'The total tip amount is ${total_tip:.2f}')
print(f'The total amount each person should pay is ${each_person_pay:.2f}')
