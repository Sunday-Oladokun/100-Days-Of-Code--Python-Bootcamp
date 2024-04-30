# Day 3: Rollercoaster Pricing Flow

print('Welcome to the rollercoaster ride pricing system')

# Take the height input in cm
height = float(input('What is your height in cm?\n'))

# Initiate the flow for deciding the ride to be paid based on height
if height >= 120:
    
    # Initiate the flow for deciding the price to be paid based on age
    
    # Take the age input
    age = int(input('What is your age?\n'))
    
    # Check if they would love to take pictures
    photos = input('Do you want pictures? Yes or No\n').lower()

    if age >= 18:
        bill = 12
        if photos == 'yes':
            print(f'You can ride the rollercoaster, pay ${bill + 3} to the cashier')
        else:
            print(f'You can ride the rollercoaster, pay {bill} to the cashier')
            
    elif age >= 12 and age < 18:
        bill = 7
        if photos == 'yes':
            print(f'You can ride the rollercoaster, pay ${bill + 3} to the cashier')
        else:
            print(f'You can ride the rollercoaster, pay {bill} to the cashier')

    else:
        bill = 5
        if photos == 'yes':
            print(f'You can ride the rollercoaster, pay ${bill + 3} to the cashier')
        else:
            print(f'You can ride the rollercoaster, pay ${bill} to the cashier')
else:
    print('You do not meet the required height of 120cm to ride the rollercoaster')