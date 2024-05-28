# Day 5: Sum of even numbers

# Take the target number
range_input = int(input('Enter a number you want to sum the even numbers for:\n4'))

# Initialize an accummulator
summation_even = 0

# Create a loop that sums the even numbers in the target number
for num in range(0, (range_input+1)):
    if num % 2 == 0:
        summation_even += num

# Print the sum
print(summation_even)