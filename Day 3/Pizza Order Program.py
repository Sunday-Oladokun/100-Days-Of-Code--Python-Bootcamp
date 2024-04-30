# Day 3: Pizza Order Program

# print("Thank you for choosing Python Pizza Deliveries!")

# What size pizza do you want? S, M, or L
size = input('What size of Pizza do you want? S, M, OR L\n').upper()
# Do you want pepperoni? Y or N
add_pepperoni = input('Do you want pepperoni? Y or N\n').upper()
# Do you want extra cheese? Y or N
extra_cheese = input('Do you want extra cheese? Y or N\n').upper()

# Initiate bill, pepperoni, and cheese prices
bill = 0
pepperoni = 2
m_l_pepperoni = 3
extra_chees = 1

# Flow for Small Pizza Order
if size == "S":
  bill = 15
  
  if add_pepperoni == "Y" and extra_cheese == "Y":
    bill += pepperoni + extra_chees
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is: ${bill}.")

  if add_pepperoni == "N" and extra_cheese == "Y":
    bill += extra_chees
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is: ${bill}.")

  if extra_cheese == "N" and add_pepperoni == "Y":
    bill += pepperoni
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is: ${bill}.")

  if extra_cheese == "N" and add_pepperoni == "N":
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is: ${bill}.")

# Flow for Medium Pizza Order 
elif size == "M":
  bill = 20
  
  if add_pepperoni == "Y" and extra_cheese == "Y":
    bill += m_l_pepperoni + extra_chees
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is: ${bill}.")

  if add_pepperoni == "N" and extra_cheese == "Y":
    bill += extra_chees
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is: ${bill}.")

  if extra_cheese == "N" and add_pepperoni == "Y":
    bill += m_l_pepperoni
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is: ${bill}.")

  if extra_cheese == "N" and add_pepperoni == "N":
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is: ${bill}.")

# Flow for Large Pizza Order
else:
  bill = 25
  
  if add_pepperoni == "Y" and extra_cheese == "Y":
    bill += m_l_pepperoni + extra_chees
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is: ${bill}.")

  if add_pepperoni == "N" and extra_cheese == "Y":
    bill += extra_chees
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is: ${bill}.")

  if extra_cheese == "N" and add_pepperoni == "Y":
    bill += m_l_pepperoni
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is: ${bill}.")

  if extra_cheese == "N" and add_pepperoni == "N":
    print("Thank you for choosing Python Pizza Deliveries!")
    print(f"Your final bill is: ${bill}.")