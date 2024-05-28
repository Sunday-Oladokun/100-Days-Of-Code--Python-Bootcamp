# Day 5: FizzBuzz Game

# Take limit input for the game
limit = int(input("Enter the number limit for the game\n"))

# Create a loop to check conditions
for num in range(0, (limit + 1)):
    
    if (num % 3 == 0) and (num % 5 == 0): # number divisible by 3 and 5:
        print('FizzBuzz')
    
    elif num % 3 == 0: # number divisible by 3
        print('Fizz')
        
    elif num % 5 == 0: # number divisible by 5
        print('Buzz')
            
    else: # number not divisible by 3 and 5
        print(num)