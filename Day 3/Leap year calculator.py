# Day 3: Leap year calculator

# Enter the year
year = int(input('Enter the year you want to check:\n'))

# Initiate a flow to check the year for leap year parameters
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year')
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is not a leap year')
else:
    print(f'{year} is not a leap year')
