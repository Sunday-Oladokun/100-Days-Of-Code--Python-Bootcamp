# Day 3: Odd or even number checker

print('Welcome to the odd/even number checker')

# Initialize a while loop that keeps running
while True:
    
    # Take user input
    user_input = input('Enter the number to be tested: ')

    # Try the number entered to confirm if its a numerical value or not
    try:
        number = float(user_input)
    except ValueError:
        print('Error: Invalid input. Please enter a numerical value.')
    
    # If the entry is numerical, Initiate a loop to check for even or odd number
    else:
        if number.is_integer():
            number = int(number)  # Convert to integer if it's a whole number

        if number % 2 == 0:
            print(f'{number} is an even number.')
        else:
            print(f'{number} is an odd number.')
        break
