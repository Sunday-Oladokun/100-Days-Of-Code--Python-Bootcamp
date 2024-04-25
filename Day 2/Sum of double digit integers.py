# DAY 2: Program that takes two integer inputs and returns their sum

# Initialize an input function requesting for a 2 digit number
two_digit_number = input("Enter a two digit number\n")
# Cast the input as a string so you can index it
str_two_digit_number = str(two_digit_number)
# Sum the indexed values by casting them in an integer for summation to work... If you don't do this, the two digits will be concatenated
summation = (int(str_two_digit_number[0]) + int(str_two_digit_number[1]))
# Print final result
print(summation)

 

